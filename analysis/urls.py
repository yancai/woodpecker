#!/usr/bin/python
# -*- coding:utf-8 -*-
# Filename: 'urls.py'

"""Documentation"""
from django.conf.urls import include, url
from analysis.views import AnalysisListView, AnalysisChartView

urlpatterns = [
    # Examples:
    # url(r'^$', 'woodpecker.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', AnalysisListView.as_view(), name="analysis_list"),
    url(r'^(P<chart_id>\d)/', AnalysisChartView.as_view(), name="analysis_chart"),

]

if __name__ == "__main__":
    pass