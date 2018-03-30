from datetime import datetime
import re
class searchDataTypes:
    def __init__(self):
        self.formats = ["%b %d %H:%M:%S", "%Y/%m/%d" ]
        self.datatypes = [
        (int, int),
        (float, float),
        (datetime, lambda value: datetime.strptime(value, self.formats[0])),
        (datetime, lambda value: datetime.strptime(value, self.formats[1])),
        (datetime, lambda value: datetime.strptime(value, "%Y/%m/%d %H:%M")),
        (datetime, lambda value: datetime.strptime(value, "%Y/%m/%d %H:%M:%S")),
        (datetime, lambda value: datetime.strptime(value, "%Y%m%d")),
        (datetime, lambda value: datetime.strptime(value, "%Y%m%d %H%M")),
        (datetime, lambda value: datetime.strptime(value, "%Y%m%d %H%M%S")),
        (datetime, lambda value: datetime.strptime(value, "%Y-%m-%d")),
        (datetime, lambda value: datetime.strptime(value, "%Y-%m-%d %H:%M")),
        (datetime, lambda value: datetime.strptime(value, "%Y-%m-%d %H:%M:%S")),
        (datetime, lambda value: datetime.strptime(value, "%d/%m/%Y")),
        (datetime, lambda value: datetime.strptime(value, "%d/%m/%Y %H:%M")),
        (datetime, lambda value: datetime.strptime(value, "%d/%m/%Y %H:%M:%S")),
        (datetime, lambda value: datetime.strptime(value, "%d-%m-%Y")),
        (datetime, lambda value: datetime.strptime(value, "%d-%m-%Y %H:%M")),
        (datetime, lambda value: datetime.strptime(value, "%d-%m-%Y %H:%M:%S")),
        (datetime, lambda value: datetime.strptime(value, "%d%m%Y")),
        (datetime, lambda value: datetime.strptime(value, "%d%m%Y %H:%M")),
        (datetime, lambda value: datetime.strptime(value, "%d%m%Y %H:%M:%S")),
        (datetime, lambda value: datetime.strptime(value, "%d%m%Y %H%M%S")),
        (datetime, lambda value: datetime.strptime(value, "%m%d%Y")),
        (datetime, lambda value: datetime.strptime(value, "%m%d%Y %H:%M")),
        (datetime, lambda value: datetime.strptime(value, "%m%d%Y %H:%M:%S")),
        (datetime, lambda value: datetime.strptime(value, "%d-%B-%Y")),
        (datetime, lambda value: datetime.strptime(value, "%d-%B-%Y %H:%M")),
        (datetime, lambda value: datetime.strptime(value, "%d-%B-%Y %H:%M:%S")),
        (datetime, lambda value: datetime.strptime(value, "%d-%b-%Y")),
        (datetime, lambda value: datetime.strptime(value, "%d-%b-%Y %H:%M")),
        (datetime, lambda value: datetime.strptime(value, "%d-%b-%Y %H:%M:%S")),
        (datetime, lambda value: datetime.strptime(value, "%d%b%Y")),
        (datetime, lambda value: datetime.strptime(value, "%d%b%Y %H:%M")),
        (datetime, lambda value: datetime.strptime(value, "%d%b%Y %H:%M:%S"))
        ]

    def __getType__(self,value):
        for typ, datatype in self.datatypes :
            try:
                datatype(value)
                typ = str(typ).split("'")[1].split(".")[0]
                if typ == "datetime":
                    dateFormat = self.__getDateFormat__(value)
                    dateFormat = re.sub("%b","Mon",dateFormat)
                    dateFormat = re.sub("%d", "DD",dateFormat)
                    dateFormat = re.sub("%m", "MM",dateFormat)
                    dateFormat = re.sub("%H", "HH24",dateFormat)
                    dateFormat = re.sub("%M", "MI",dateFormat)
                    dateFormat = re.sub("%S", "SS",dateFormat)
                    dateFormat = re.sub("%Y", "YYYY",dateFormat)

                    typ = typ + "#"  + dateFormat
                return typ
            except ValueError:
                continue
        return "str"


    def __getDateFormat__(self,value):
        for format in self.formats :
        #print(format)
            try:
                datetime.strptime(value, format)
                return format
            except ValueError:
                continue
#a = getType(2134)
#print(a)
#a = getType('Feb 22 05:58:51')
#print(a)

#value = 'Feb 22 05:58:51'

#if a.find('datetime') != -1:
#    dataType = "DATE"
#    ctlDataType = "DATE " + a.split('#')[1]
#    print(ctlDataType)


#print(getType('2010/1/12'))
#print(getType('2010.2'))
#print(getType('2010'))
#print(getType('2013test'))
#print(getType('12-JAN-2012 12:32:43'))
#print(getType('12012017 123243'))

