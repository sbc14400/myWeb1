from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from .models import Post, Device
from .forms import PostForm, DeviceForm


def post_devicelist(request):
    devices = Device.objects.order_by('InputDate')
    return render(request, 'blog/post_devicelist.html', {'devices': devices})

    # device=sqlite3.connect(database='db.sqlite3')
    # cursor=device.cursor()
    # cursor.execute('SELECT DeviceID from amst_Device')
    # devices=[row[0] for row in cursor.fetchall()]
    # return render(request, 'blog/post_list.html',{'posts':devices})


def post_devicedetail(request, pk):
    device=get_object_or_404(Device, pk=pk)
    return render(request, 'blog/post_devicedetail.html', {'device': device})


def post_devicenew(request):
    if request.method == "POST":
        form = DeviceForm(request.POST)
        if form.is_valid():
            device = form.save(commit=False)
            device.author = request.user
            device.published_date = timezone.now()
            device.save()
            return redirect('post_devicedetail', pk=device.pk)
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

