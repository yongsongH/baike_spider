'''
Created on 2016-4-15

@author: hys mac
'''
class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def output(self):
        fout = open('output.html', 'w')

        fout.write("<html>")
        fout.write("<body")
        fout.write("<table")
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'].encode('utf-8'))
            fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))
            fout.write("</tr>")
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")

        fout.close()

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)
    
    
    



