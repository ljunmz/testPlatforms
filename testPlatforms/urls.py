"""testPlatforms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.views.static import serve

from apitest.views import apitest, getFlowData, getNodeData, getOutSql, getPreSql, getPostKey, getParameter, addFlow, \
    editFlow, deleteFlow, addNode, editNode, savePostKey, editParameter, deleteNode, editOutSql, editPreSql, getCreater, \
    actionFlow, getEmail, emailChange, actionAllFlow, changeFlowState, changeNodeState, editDefaultVar, getDefaultVar, \
    deleteDefaultVar, addDefaultVar
from sql.views import sqlIndex, register, clearModelCodeRecords, clearPhoneCodeRecords, changeCreatedTime, getUserInfo, \
    getTokenInfo, getTodoInfo
from testPlatforms import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^index', apitest),
    url(r'^getFlowData', getFlowData),
    url(r'^getNodeData', getNodeData),
    url(r'^getOutSql', getOutSql),
    url(r'^getPreSql', getPreSql),
    url(r'^getPostKey', getPostKey),
    url(r'^getParameter', getParameter),
    url(r'^addFlow', addFlow),
    url(r'^editFlow', editFlow),
    url(r'^deleteFlow', deleteFlow),
    url(r'^deleteNode', deleteNode),
    url(r'^addNode', addNode),
    url(r'^editNode', editNode),
    url(r'^savePostKey', savePostKey),
    url(r'^editParameter', editParameter),
    url(r'^editOutSql', editOutSql),
    url(r'^editPreSql', editPreSql),
    url(r'^getCreater', getCreater),
    url(r'^actionFlow', actionFlow),
    url(r'^sqlIndex', sqlIndex),
    url(r'^register', register),
    url(r'^clearModelCodeRecords', clearModelCodeRecords),
    url(r'^clearPhoneCodeRecords', clearPhoneCodeRecords),
    url(r'^changeCreatedTime', changeCreatedTime),
    url(r'^getUserInfo', getUserInfo),
    url(r'^getTokenInfo', getTokenInfo),
    url(r'^getTodoInfo', getTodoInfo),
    url(r'^getEmail', getEmail),
    url(r'^emailChange', emailChange),
    url(r'^actionAllFlow', actionAllFlow),
    url(r'^changeFlowState', changeFlowState),
    url(r'^changeNodeState', changeNodeState),
    url(r'^deleteDefaultVar', deleteDefaultVar),
    url(r'^addDefaultVar', addDefaultVar),
    url(r'^editDefaultVar', editDefaultVar),
    url(r'^getDefaultVar', getDefaultVar),
    # url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_URL}),
]
