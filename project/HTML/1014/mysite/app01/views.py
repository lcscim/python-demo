#__author__:asus
#date:2018/10/14
from django.shortcuts import render,redirect,HttpResponse
import pymysql
from helper import mysqlhelp
import json
def classes(req):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='s4db65',charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("select id,title from class")
    class_list=cursor.fetchall()
    cursor.close()
    conn.close()
    return render(req,"classes.html",locals())
def add_class(req):
    if req.method=="GET":
        return render(req,"add_class.html")
    else:
        v=req.POST.get("add_class")
        if len(v.strip())>0:
            conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='s4db65', charset='utf8')
            cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
            cursor.execute("insert into class(title) values (%s)",v)
            conn.commit()
            cursor.close()
            conn.close()
        else:
            return render(req,"add_class.html",{"msg":'不能为空'})


def del_class(req):
    nid = req.GET.get('nid')
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='s4db65', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("delete from class where id=%s", nid)
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/classes/')
def edit_class(req):
    if req.method=="GET":
        nid = req.GET.get('nid')
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='s4db65', charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("select id,title from class where id=%s", nid)
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return render(req, "edit_class.html",{'result':result})
    else:
        nid = req.GET.get('nid')
        title = req.POST.get('edit_class')
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='s4db65', charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("update class set title=%s where id=%s", [title,nid,])
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/classes/')
def students(req):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='s4db65',charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("SELECT student.id,student.`name`,student.class_id,class.title FROM student LEFT JOIN class ON student.class_id=class.id")
    student_list=cursor.fetchall()
    cursor.close()
    conn.close()
    class_list=mysqlhelp.get_list('select id,title from class')
    return render(req,"students.html",{'student_list':student_list,'class_list':class_list})
def add_student(req):
    if req.method=="GET":
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='s4db65', charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("select id,title from class")
        class_list = cursor.fetchall()
        cursor.close()
        conn.close()
        return render(req,"add_student.html",{'class_list':class_list})
    else:
        name = req.POST.get('name')
        class_id = req.POST.get('class_id')
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='s4db65', charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute(
            "insert into student(name,class_id) values (%s,%s)",[name,class_id])
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/students/')
def del_student(req):
    nid = req.GET.get('nid')
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='s4db65', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("delete from student where id=%s", nid)
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/students/')
def edit_student(req):
    if req.method=="GET":
        nid = req.GET.get('nid')
        class_list = mysqlhelp.get_list("select id,title from class")
        current_student_info = mysqlhelp.get_one('select id,name,class_id from student where id=%s',[nid,])
        return render(req,"edit_student.html",{"class_list":class_list,"current_student_info":current_student_info})
    else:
        nid = req.GET.get('nid')
        name = req.POST.get('name')
        class_id = req.POST.get('class_id')
        mysqlhelp.set_list('update student set name=%s,class_id=%s where id=%s',[name,class_id,nid])
        return redirect('/students/')

def modal_add_class(req):
    title=req.POST.get('title')
    print(title)
    if len(title) > 0:
        # mysqlhelp.set_list('insert into class(title) values(%s)',[title,])
        # return redirect('/classes/')
        # form表单提交会刷新页面，就会使拟态对话框刷新，此时用ajax
        mysqlhelp.set_list('insert into class(title) values(%s)', [title, ])
        return HttpResponse("ok")
    else:
        return HttpResponse("班级标题不能为空")
def modal_edit_class(req):
    ret = {'status':True,'message':None}
    try:
        nid= req.POST.get('nid')
        content=req.POST.get('content')
        mysqlhelp.set_list('update class set title=%s where id=%s',[content,nid,])
    except Exception as e:
        ret['status']=False
        ret['message']=str(e)
    return HttpResponse(json.dumps(ret))
def modal_add_student(req):
    ret = {'status': True, 'message': None}
    try:
        nid= req.POST.get('nid')
        name=req.POST.get('name')
        mysqlhelp.set_list('insert into student(name,class_id) values (%s,%s)',[name,nid,])
    except Exception as e:
        ret['status']=False
        ret['message']=str(e)
    return HttpResponse(json.dumps(ret))
def modal_edit_student(req):
    ret = {'status': True, 'message': None}
    try:
        nid = req.POST.get('nid')
        name = req.POST.get('name')
        class_id=req.POST.get('class_id')
        mysqlhelp.set_list('update student set name=%s,class_id=%s where id=%s', [name, class_id,nid,])
    except Exception as e:
        ret['status'] = False
        ret['message'] = str(e)
    return HttpResponse(json.dumps(ret))
def teachers(req):
    teacher_list=mysqlhelp.get_list("""
        SELECT teacher.id AS tid,teacher.name,class.title FROM teacher
        LEFT JOIN teacher2class ON teacher.id = teacher2class.teacher_id
        LEFT JOIN class ON class.id = teacher2class.class_id;""")
    #print(teacher_list)
    result={}
    for row in teacher_list:
        tid=row['tid']
        if tid in result:
            result[tid]['titles'].append(row['title'])
        else:
            result[tid]={'tid':row['tid'],'name':row['name'],'titles':[row['title'],]}
    return render(req,'teachers.html',{'teacher_list':result.values()})