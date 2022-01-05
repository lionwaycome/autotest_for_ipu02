#coding=utf-8

import xlrd
import xml.dom.minidom
#from lxml import etree
import time
    
class xmlTOhtml:
    

    def __init__(self):
        self.workbook = xlrd.open_workbook("D:\\TestStand_IPU02\\IPU02_System Verification Test Specification-autotest.xlsx")
        self.table=self.workbook.sheet_by_name("TC-1")
##        self.lineALL=[]
        self.route = "D:\\TestStand_IPU02\\report\\自动化测试报告["+time.strftime("%Y-%#m-%#d",time.localtime(time.time()))+"]"
        self.f_xml = open(self.route +'.xml')
        self.ff_xml=self.f_xml.read()
        self.f_xml.close()

   
          
        
       

##    def read_excel_ID(self,row):
##        row1=self.table.cell(2,row).value
##        num=2
##        lineALL=[]
##        while 1:
##            
##            linenum = self.table.cell(num,row).value
##            if linenum:
##                lineALL.append(linenum)
##                num+=1
##            else:
##                self.lineALL=lineALL
##
##                #print(lineALL)
##                #print(num)
##                break
        

        

    def GetResult(self,ID):
        CaseResult=dict()
        pos=self.ff_xml.find(ID) 
        pos2=self.ff_xml.find('</tr:Test>',pos)
        head=self.ff_xml[pos:pos2]
        Result_Data=head.find('<tr:Outcome value = "Passed" />')
        if Result_Data != -1:
            Result="Passed"
        else:
            Result="Failed"

        pos_TestResult1=head.find('<tr:TestResult ID')
        pos_TestResult2=head.find('</tr:TestResult>')
        Des=head[pos_TestResult1:pos_TestResult2]


        pos_TestData1=Des.find('<tr:TestData>')
        pos_TestData2=Des.find('</tr:TestData>')
        Testdata=Des[pos_TestData1:pos_TestData2]


        pos_Value1=Testdata.find('<c:Value>') + 9
        pos_Value2=Testdata.find('</c:Value>')
        Describtion=Testdata[pos_Value1:pos_Value2]

        CaseResult={"Result":Result,"Describtion":Describtion}
        #print(CaseResult)
        return CaseResult







    

    def read_excel(self,row):
        lineALL=""
        for num in range(2,self.table.nrows):
            ID = self.table.cell(num,row).value.replace('\n', '')
##            print(num)
##            print(ID)
            CaseResult=self.GetResult(ID)
            Describtion = CaseResult['Describtion']
            if Describtion == "":
                Describtion = "Error! No result return"
            Result=CaseResult['Result']
            #print(CaseResult)
            if Result == 'Passed':
                color = 'green'
            else:
                color = 'red'
            
            line ='<tr><td align="center">' + str(num-1) + '</td>'\
                   + '<td align="center">'+ self.table.cell(num,1).value + '</td>' \
                   + '<td align="center">'+ ID + '</td>' \
                   + '<td align="left">' + self.table.cell(num,2).value + '</td>' \
                   + '<td align="left">' + self.table.cell(num,3).value + '</td>' \
                   + '<td align="left">' + self.table.cell(num,4).value + '</td>' \
                   + '<td align="center" style="background-color:' + color +'">' + Result + '</td>' \
                   + '<td align="left">' + Describtion + '</td></tr>'

            lineALL=lineALL+line
            num+=1

        return lineALL

    def html_Head(self):
        F_VERSION = open("D:\\TestStand_IPU02\\Version.txt")  #Read software version from Version.txt
        line = F_VERSION.readline()
        SWVersion = line.split(":",1)
        version = SWVersion[1]
        
        Time = time.strftime('%Y/%m/%d %A %H:%M:%S',time.localtime(time.time()))
        pos=self.ff_xml.find('<tr:Outcome value')
        pos2=self.ff_xml.find('tr:Test ID',pos)
        head=self.ff_xml[pos:pos2]
        fs = head.find('Passed')
        if fs != -1:
            TotalResult="Passed"
            color='green'
        else:
            TotalResult="Failed"
            color='red'

        HeadData = '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"><html><body>' \
                   + '<h1>IPU02自动冒烟测试报告</h1>' \
                   + '<table border="1" style="border-collapse: collapse;cellspacing="0"">' \
                   + '<tr>' \
                   + '<td bgcolor="#20B2AA"><font color="#FFFFFF">Time</font></td>' \
                   + '<td style="font-family: Verdana">' + Time + '</td>' \
                   + '</tr>' \
                   + '<tr>' \
                   + '<td bgcolor="#20B2AA"><font color="#FFFFFF">Software version</font></td>' \
                   + '<td style="font-family: Verdana;width:100px;word-break:keep-all">'+ version +'</td>' \
                   + '</tr>' \
                   + '<tr>' \
                   + '<td bgcolor="#20B2AA"><font color="#FFFFFF">Test result</font></td>' \
                   + '<td style="font-family: Verdana; font-size: 20px; font-weight: bold;background-color:' + color + '">' + TotalResult + '</td></table>'

        return HeadData


    def Write_HTML(self):
        
        html = open(self.route + '.html','w')
        html_FormHead = '<br/><hr><table border="1" style="border-collapse: collapse;cellspacing="0";word-break:break-all";table-layout: fixed>' \
                    +  '<tr>' \
                    + '<th bgcolor="#20B2AA"><font color="#FFFFFF">Num.</th>' \
                    + '<th bgcolor="#20B2AA"><font color="#FFFFFF">Title</th>' \
                    + '<th bgcolor="#20B2AA"><font color="#FFFFFF">TC_ID</th>' \
                    + '<th bgcolor="#20B2AA"><font color="#FFFFFF">Inital Condition</th>' \
                    + '<th bgcolor="#20B2AA"><font color="#FFFFFF">Action</th>' \
                    + '<th bgcolor="#20B2AA"><font color="#FFFFFF">Expected Result</th>' \
                    + '<th bgcolor="#20B2AA"><font color="#FFFFFF">Test Result</th>' \
                    + '<th bgcolor="#20B2AA"><font color="#FFFFFF">Describtion</th>'\
                    + '</tr>'
        html_FormHead_END = '</table></body></html>'
                                   
        html_data =self.html_Head() + html_FormHead + self.read_excel(0) + html_FormHead_END

        html.write(html_data)
        #print(html_data)

        html.close





if __name__ =="__main__":
    #GetResult()
    time.sleep(10)
    aaa=xmlTOhtml()
    #aaa.read_excel_ID(0)
    #aaa.GetResult('TC_11_Picture_0002')
    #aaa.read_excel(0)
    aaa.Write_HTML()
    #print(time.strftime('%Y/%m/%d %A %H:%M:%S',time.localtime(time.time())))

    
    
    
