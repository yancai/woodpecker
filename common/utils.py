#!/usr/bin/python
# -*- coding:utf-8 -*-
# Filename: 'utils.py'
# Author:   'yancai'
# Date:     '2015/4/16'

"""Documentation"""
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator


def slice_range(total, max_range, current):
    """

    :param total:
    :param max_range:
    :param current:
    :return:
    """
    if current <= max_range:
        start = 1
    else:
        start = current - max_range

    if total < current + max_range:
        end = total
    else:
        end = current + max_range

    return range(start, end+1)


class MyPaginator(Paginator):
    def __init__(self, object_list, per_page, orphans=0,
                 allow_empty_first_page=True, max_range=5):
        super(MyPaginator, self).__init__(object_list, per_page, orphans, allow_empty_first_page)
        self.max_range = max_range

    def page(self, number):
        self.number = self.validate_number(number)
        return super(MyPaginator, self).page(number)

    def _page_range_ext(self):
        return slice_range(self.num_pages, self.max_range, self.number)

    page_range_ext = property(_page_range_ext)


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view, login_url="/")


if __name__ == "__main__":
    total_nums = 4
    cur_num = 1
    range_num = 3
    assert cur_num <= total_nums

    print(range(1, total_nums+1))
    s = ""
    for i in slice_range(total_nums, range_num, cur_num):
        if i == cur_num:
            s += "[%s], " % i
        else:
            s += "%s, " % i
    print(s)
    pass