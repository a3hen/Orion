
# coding:utf-8
'''
Created on 2020/3/2
@author: Paul
@note: data
'''

from flask import Flask, render_template, views


class Index(views.MethodView):
    def get(self):
        return render_template("index.html")
    
class iSCSICreate(views.MethodView):
    def get(self):
        return render_template("iSCSI_create.html")

    
class Resource(views.MethodView):
    def get(self):
        return render_template("Resource.html")
