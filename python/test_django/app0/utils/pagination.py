"""
分页组件
"""

from django.utils.safestring import mark_safe


class Pagination(object):
    def __init__(self, request, queryset, page_size=10, page_param="page", plus=5):
        """
        request:    请求
        queryset:   查询数据结果
        page_size:  每页展示数量
        page_param: 页面查询参数
        plus:       页面数量
        """
        page = request.GET.get(page_param, "1")
        import copy
        self.query_dic = copy.deepcopy(request.GET)
        self.query_dic._multable = True
        self.page_param = page_param
        if page.isdecimal():
            page = int(page)
        else:
            page = 1
        self.page = page
        self.page_size = page_size
        self.start = (self.page - 1) * page_size
        self.end = self.page * page_size

        self.page_queryset = queryset[self.start: self.end]
        self.total_count = queryset.count()
        total_page_count, div = divmod(self.total_count, page_size)
        if div:
            total_page_count += 1
        self.total_page_count = total_page_count
        self.plus = plus
        #print(page, type(page))
        if self.page <= 0:
            self.page = 1
        elif self.page > self.total_page_count:
            self.total_page_count

    def html(self):
        if self.total_page_count <= 2 * self.plus + 1:
            start_page = 1
            end_page = self.total_page_count
        else:
            if self.page <= self.plus:
                start_page = 1
                end_page = 2 * self.plus + 1
            else:
                if (self.page + self.plus) > self.total_page_count:
                    start_page = self.total_page_count - 2 * self.plus + 1
                    end_page = self.total_page_count
                else:
                    start_page = self.page - self.plus
                    end_page = self.page + self.plus

        page_string_list = []
        self.query_dic.setlist(self.page_param, [1])
        first_element = '<li class="page-item"><a class="page-link" href="?{}"><span aria-hidden="true">首页</span></a></li>'.format(self.query_dic.urlencode())
        page_string_list.append(first_element)
        if self.page == 1:
            self.query_dic.setlist(self.page_param, [1])
            prev = '<li class="page-item disabled"><a class="page-link" href="?{}"><span aria-hidden="true">&laquo;</span></a></li>'.format(self.query_dic.urlencode())
        else:
            self.query_dic.setlist(self.page_param, [self.page - 1])
            prev = '<li class="page-item"><a class="page-link" href="?{}"><span aria-hidden="true">&laquo;</span></a></li>'.format(
                self.query_dic.urlencode())
        page_string_list.append(prev)
        for i in range(start_page, end_page + 1):
            self.query_dic.setlist(self.page_param, [i])
            if i == self.page:
                element = '<li class="page-item active"><a class="page-link" href="?{}"><span aria-hidden="true">{}</span></a></li>'.format(
                    self.query_dic.urlencode(), i)
            else:
                element = '<li class="page-item"><a class="page-link" href="?{}"><span aria-hidden="true">{}</span></a></li>'.format(
                    self.query_dic.urlencode(), i)
            page_string_list.append(element)

        if self.page == self.total_page_count:
            self.query_dic.setlist(self.page_param, [self.total_page_count])
            next = '<li class="page-item disabled"><a class="page-link" href="?{}"><span aria-hidden="true">&raquo;</span></a></li>'.format(
                self.query_dic.urlencode())
        else:
            self.query_dic.setlist(self.page_param,  [self.page + 1])
            next = '<li class="page-item"><a class="page-link" href="?{}"><span aria-hidden="true">&raquo;</span></a></li>'.format(
                self.query_dic.urlencode())
        page_string_list.append(next)

        self.query_dic.setlist(self.page_param, [self.total_page_count])
        end_element = '<li class="page-item"><a class="page-link" href="?{}"><span aria-hidden="true">尾页</span></a></li>'.format(
            self.query_dic.urlencode())
        page_string_list.append(end_element)



        search_string = """
                <form method="get" style="float:left; margin-left: -1px; width:120px;">
                        <div class="input-group mb-3">
                            <input type="text" class="form-control" placeholder="页码" name="page">
                            <div class="input-group-append">
                                <button class="btn btn-outline-secondary" type="submit"  aria-hidden="true">跳转</button>
                            </div>
                        </div>
                    </form>
        """

        page_string_list.append(search_string)
        page_string = mark_safe("".join(page_string_list))
        return page_string

