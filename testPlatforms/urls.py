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

from apitest.views import apitest, getFlowData, getNodeData, getOutSql, getPreSql, getPostKey, getParameter, addFlow, \
    editFlow, deleteFlow, addNode, editNode, savePostKey, editParameter, deleteNode, editOutSql, editPreSql, getCreater, \
    actionFlow, getEmail, emailChange, actionAllFlow, changeFlowState, changeNodeState, editDefaultVar, getDefaultVar, \
    deleteDefaultVar, addDefaultVar, getApiStatistics, getLog, lookDetailReport, lookSummaryReport, filterFlowName, \
    filterPath
from performance.views import performance, \
    getPerformanceFlowData, getPerformanceNodeData, getPerformanceOutSql, getPerformancePreSql, getPerformancePostKey, \
    getPerformanceParameter, addPerformanceFlow, editPerformanceFlow, deletePerformanceFlow, deletePerformanceNode, \
    addPerformanceNode, editPerformanceNode, savePerformancePostKey, editPerformanceParameter, editPerformanceOutSql, \
    editPerformancePreSql, getPerformanceCreater, actionPerformanceFlow, getPerformanceEmail, performanceEmailChange, \
    actionPerformanceAllFlow, changePerformanceFlowState, changePerformanceNodeState, deletePerformanceDefaultVar, \
    addPerformanceDefaultVar, editPerformanceDefaultVar, getPerformanceDefaultVar, getPerformanceConfig,  \
    savePerformanceConfig
from plan.views import plan
from sql.views import sqlIndex, register, clearModelCodeRecords, clearPhoneCodeRecords, changeCreatedTime, getUserInfo, \
    getTokenInfo, getTodoInfo, getBuriedInfo
from task.views import startWork, startBeat
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'index', apitest),
    url(r'getFlowData', getFlowData),
    url(r'getNodeData', getNodeData),
    url(r'getOutSql', getOutSql),
    url(r'getPreSql', getPreSql),
    url(r'getPostKey', getPostKey),
    url(r'getParameter', getParameter),
    url(r'addFlow', addFlow),
    url(r'editFlow', editFlow),
    url(r'deleteFlow', deleteFlow),
    url(r'deleteNode', deleteNode),
    url(r'addNode', addNode),
    url(r'editNode', editNode),
    url(r'savePostKey', savePostKey),
    url(r'editParameter', editParameter),
    url(r'editOutSql', editOutSql),
    url(r'editPreSql', editPreSql),
    url(r'getCreater', getCreater),
    url(r'actionFlow', actionFlow),
    url(r'sqlIndex', sqlIndex),
    url(r'register', register),
    url(r'clearModelCodeRecords', clearModelCodeRecords),
    url(r'clearPhoneCodeRecords', clearPhoneCodeRecords),
    url(r'changeCreatedTime', changeCreatedTime),
    url(r'getUserInfo', getUserInfo),
    url(r'getTokenInfo', getTokenInfo),
    url(r'getTodoInfo', getTodoInfo),
    url(r'getEmail', getEmail),
    url(r'emailChange', emailChange),
    url(r'actionAllFlow', actionAllFlow),
    url(r'changeFlowState', changeFlowState),
    url(r'changeNodeState', changeNodeState),
    url(r'deleteDefaultVar', deleteDefaultVar),
    url(r'addDefaultVar', addDefaultVar),
    url(r'editDefaultVar', editDefaultVar),
    url(r'getDefaultVar', getDefaultVar),
    url(r'getBuriedInfo', getBuriedInfo),
    url(r'startWork', startWork),
    url(r'startBeat', startBeat),
    url(r'performance', performance),
    url(r'getPerformanceFlowData', getPerformanceFlowData),
    url(r'getPerformanceNodeData', getPerformanceNodeData),
    url(r'getPerformanceOutSql', getPerformanceOutSql),
    url(r'getPerformancePreSql', getPerformancePreSql),
    url(r'getPerformancePostKey', getPerformancePostKey),
    url(r'getPerformanceParameter', getPerformanceParameter),
    url(r'addPerformanceFlow', addPerformanceFlow),
    url(r'editPerformanceFlow', editPerformanceFlow),
    url(r'deletePerformanceFlow', deletePerformanceFlow),
    url(r'deletePerformanceNode', deletePerformanceNode),
    url(r'addPerformanceNode', addPerformanceNode),
    url(r'editPerformanceNode', editPerformanceNode),
    url(r'savePerformancePostKey', savePerformancePostKey),
    url(r'editPerformanceParameter', editPerformanceParameter),
    url(r'editPerformanceOutSql', editPerformanceOutSql),
    url(r'editPerformancePreSql', editPerformancePreSql),
    url(r'getPerformanceCreater', getPerformanceCreater),
    url(r'actionPerformanceFlow', actionPerformanceFlow),
    url(r'getPerformanceEmail', getPerformanceEmail),
    url(r'performanceEmailChange', performanceEmailChange),
    url(r'actionPerformanceAllFlow', actionPerformanceAllFlow),
    url(r'changePerformanceFlowState', changePerformanceFlowState),
    url(r'changePerformanceNodeState', changePerformanceNodeState),
    url(r'deletePerformanceDefaultVar', deletePerformanceDefaultVar),
    url(r'addPerformanceDefaultVar', addPerformanceDefaultVar),
    url(r'editPerformanceDefaultVar', editPerformanceDefaultVar),
    url(r'getPerformanceDefaultVar', getPerformanceDefaultVar),
    url(r'getPerformanceConfig', getPerformanceConfig),
    url(r'savePerformanceConfig', savePerformanceConfig),
    url(r'plan', plan),
    url(r'getApiStatistics', getApiStatistics),
    url(r'lookDetailReport', lookDetailReport),
    url(r'lookSummaryReport', lookSummaryReport),
    url(r'getLog', getLog),
    url(r'filterFlowName', filterFlowName),
    url(r'filterPath', filterPath),
    # url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_URL}),
]
