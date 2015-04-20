#!/usr/bin/python
# -*- coding:utf-8 -*-
# Filename: 'views.py'

"""Documentation"""
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from common.utils import LoginRequiredMixin


class AnalysisListView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return HttpResponse(render(request, "analysis/analysis_list.html"))


class AnalysisChartView(View):

    def get(self, request):
        # TODO
        pass

    def post(self, request):
        # TODO
        pass

if __name__ == "__main__":
    pass