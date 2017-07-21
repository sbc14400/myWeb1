from django.shortcuts import render, get_object_or_404, redirect, HttpResponse, render_to_response, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import timezone
from .models import Post, Device, PadInfo
from .forms import PostForm, DeviceForm

# from django_datatables_view.base_datatable_view import BaseDatatableView
from django.http import JsonResponse
from django.core import  serializers
import datetime
from django.contrib.auth import authenticate, login
import json

from chartit import DataPool, Chart
from highcharts.views import *


# class TableDevice(BaseDatatableView):
#     model = Device
#     columns = ['DeviceID', 'CustomerProduct', 'Tester', 'NoPara', 'ProductType', 'InputDate']
#     order_columns = ['DeviceID', 'InputData']
#     max_display_length = 500
#
#
#     def render_column(self, row, column):
#
#         if column == 'user':
#             return '{0} {1}'.format(row.customer_firstname, row.customer_lastname)
#         else:
#             return super(TableDevice, self).render_column(row, column)

        # return render(request, '/', {'devices': devices})


    # def filter_queryset(self, qs):
    #     # use parameters passed in GET request to filter queryset
    #
    #     # simple example:
    #     search = self.request.GET.get(u'search[value]', None)
    #     if search:
    #         qs = qs.filter(name__istartswith=search)
    #
    #     # more advanced example using extra parameters
    #     filter_customer = self.request.GET.get(u'customer', None)
    #
    #     if filter_customer:
    #         customer_parts = filter_customer.split(' ')
    #         qs_params = None
    #         for part in customer_parts:
    #             q = Q(customer_firstname__istartswith=part) | Q(customer_lastname__istartswith=part)
    #             qs_params = qs_params | q if qs_params else q
    #         qs = qs.filter(qs_params)
    #     return qs

def post_devicelist(request):
    devices = Device.objects.order_by('-pk')
    return render(request, 'blog/post_devicelist.html', {'devices': devices})
    # device=sqlite3.connect(database='db.sqlite3')
    # cursor=device.cursor()
    # cursor.execute('SELECT DeviceID from amst_Device')
    # devices=[row[0] for row in cursor.fetchall()]
    # return render(request, 'blog/post_list.html',{'posts':devices})



def post_devicedetail(request, pk):
    device=get_object_or_404(Device, pk=pk)
    return render(request, 'blog/post_devicedetail.html', {'device': device})

def ajax_devicedetail(request):

    if request.method == 'POST':
        if request.is_ajax():
            data = request.POST['pkDevice']
            device_list = Device.objects.filter(id=data)
            device = serializers.serialize("json", device_list)
            # print(device)

            # result = json.parse(device)
            # print(result[0].fields.DeviceID)

            return JsonResponse(device, safe=False)
    return render(request)

            # print(data)
            # device_list = Device.objects.all()

            # device_list = get_object_or_404(Device, pk=data)
            # print(device_list.DeviceID)
            # print(device_list.ProductType)

            # return HttpResponse(device, content_type='application/json')
            # return JsonResponse(device)
            # str = "<html><b> you sent an ajax post request </b> <br> returned data: %s</html>" % data
            # return HttpResponse(astr)


def ajax_paddetail(request):

    if request.method == 'POST':
        if request.is_ajax():

            pkDevice = request.POST['DeviceID']
            bolnc = request.POST['bolnc']

            # print(bolnc)
            if bolnc == "true":
                device_list = PadInfo.objects.filter(DeviceID=pkDevice)
            else:
                device_list = PadInfo.objects.filter(DeviceID=pkDevice).exclude(Function='nc')

            device = serializers.serialize("json", device_list)
            # print(device)

            # result = json.parse(device)
            # print(result[0].fields.DeviceID)

            return JsonResponse(device, safe=False)
    return render(request)

            # print(data)
            # device_list = Device.objects.all()

            # device_list = get_object_or_404(Device, pk=data)
            # print(device_list.DeviceID)
            # print(device_list.ProductType)

            # return HttpResponse(device, content_type='application/json')
            # return JsonResponse(device)
            # str = "<html><b> you sent an ajax post request </b> <br> returned data: %s</html>" % data
            # return HttpResponse(astr)



def ajax_chart_pad(request):

    # if request.method == 'GET':
    #     return render(request)

    # Step 1: Create a DataPool with the data we want to retrieve.
    pkDevice = request.POST['DeviceID']
    bolnc = request.POST['bolnc']


    if bolnc == "true":
        device_list = PadInfo.objects.filter(DeviceID=pkDevice)
        _str='(with NC)'
    else:
        device_list = PadInfo.objects.filter(DeviceID=pkDevice).exclude(Function='nc')
        _str='(no NC)'

    padData = DataPool(\
        series=
        [{'options': {
            'source': device_list},
            'terms': [
                'PadX',
                'PadY']}
        ])

    cht = Chart(
        datasource=padData,
        series_options=
        [{'options': {
            'type': 'scatter',
            'stacking': False},
            'terms': {
                'PadX': [
                    'PadY']
            }}],
        chart_options=
        {'title': {
            'text': pkDevice + '  Pad' + _str},
            'xAxis': {
                'title': {
                    'text': 'PadX'}}})
    # Step 2: Create the Chart object

    # Step 3: Send the chart object to the template.
    print(cht.to_json())
    return JsonResponse(cht.to_json(), safe=False)
    # return render_to_response({'padchart': cht})


def post_devicenew(request):
    if request.method == "POST":
        form = DeviceForm(request.POST)
        if form.is_valid():
            device = form.save(commit=False)
            device.author = request.user
            device.published_date = timezone.now()
            device.save()

            devices = Device.objects.order_by('-pk')
            return render(request, 'blog/post_devicelist.html', {'devices': devices})
            # post_devicelist()
            # return redirect(request, 'blog/post_devicelist.html')
    else:
        form = DeviceForm()
    return render(request, 'blog/post_deviceedit.html', {'form': form})


def post_deviceedit(request, pk):
    device = get_object_or_404(Device, pk=pk)
    if request.method == "POST":
        form = DeviceForm(request.POST, instance=device)
        if form.is_valid():
            device = form.save(commit=False)
            # device.CustomerProduct = request.CustomerProduct
            # device.Tester = request.Tester
            # device.NoPara = request.NoPara
            device.InputDate = timezone.now()
            device.save()
            return redirect('post_devicedetail', pk=device.pk)
    else:
        form = DeviceForm(instance=device)
    return render(request, 'blog/post_deviceedit.html', {'form': form})



def post_pgmnote(request):
    return render(request, 'blog/post_pgmnote.html')

def post_list(request):
    posts=Post.objects.order_by('published_date')
    # posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})


def post_detail(request, pk):
    post=get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

