from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger



def get_pagination(request,obj,size):
    paginator = Paginator( obj,size,orphans=0, allow_empty_first_page=True)
    page_number = request.GET.get("page")
    try:
        items = paginator.page(page_number)
    except PageNotAnInteger:
        page_number = 1
        items = paginator.page(page_number)
    except EmptyPage:
        page_number = paginator.num_pages
        items = paginator.page(page_number)

    return items

