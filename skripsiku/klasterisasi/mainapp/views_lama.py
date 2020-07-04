import csv, io, logging
from pprint import pprint
import math, random
from django.contrib import messages
from django import forms
import json, datetime
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.generic import CreateView, DetailView, ListView, DeleteView, UpdateView, FormView
from django.template.loader import render_to_string
from .models import Post
from .forms import KecamatanForm, DataForm, BPForm
from django.urls import reverse


# Create your views here.
hasil = ""

def home(request):
    return render(request, 'mainapp/home.html', {'title': 'Hello'})

def klasterisasi(request):
    terpilih = ""
    terpilih1 = ""
    pilihcluster1 = ""
    pilihcluster2 = ""
    pCluster1 = []
    pCluster2 = []

    jarakCluster1 = []
    jarakCluster2 = []

    anggotaC1 = []
    anggotaC2 = []

    terbobot1 = []
    terbobot2 = []

    final1 = []
    final2 = []
    
    dataAwal = {}
    if request.method == 'POST':
        kecForm = KecamatanForm(request.POST)
        bpForm = BPForm(request.POST)
        terpilih = request.POST.get('pilihKecamatan')
        terpilih1 = request.POST.get('bp')
        dataAwal = Post.objects.filter(pilihKecamatan__contains=terpilih, bp__contains=terpilih1)
        
        pilihcluster1 = random.choice(dataAwal)
        pilihcluster2 = random.choice(dataAwal)

        while True:
            if pilihcluster1 != pilihcluster2:
                break

            pilihcluster1 = random.choice(dataAwal)
            pilihcluster2 = random.choice(dataAwal)
        
        if pilihcluster1 != None and pilihcluster2 != None:
            # pCluster1 = Post.objects.filter(namaSekolah__contains=pilihcluster1)
            # pCluster2 = Post.objects.filter(namaSekolah__contains=pilihcluster2)

            pCluster1 = pilihcluster1
            pCluster2 = pilihcluster2

            for jarak1 in dataAwal:
                nama1 = jarak1.namaSekolah
                jaraknya1 = (((jarak1.guru - pCluster1.guru)**2) + ((jarak1.rKelas - pCluster1.rKelas)**2) + ((jarak1.rLab - pCluster1.rLab)**2) +((jarak1.rPerpus - pCluster1.rPerpus)**2) + ((jarak1.rasioPDRB - pCluster1.rasioPDRB)**2) + ((jarak1.rasioGRB - pCluster1.rasioGRB)**2))
                jarakCluster1.append({'namaSekolah' : nama1, 'X1' : jarak1.guru, 'X2' : jarak1.rKelas,'X3' : jarak1.rLab,'X4' : jarak1.rPerpus,'X5' : jarak1.rasioPDRB,'X6' : jarak1.rasioGRB, 'jarak' : jaraknya1, 'kelompok' : 0})

            for jarak2 in dataAwal:
                nama2 = jarak2.namaSekolah
                jaraknya2 = (((jarak2.guru - pCluster2.guru)**2) + ((jarak2.rKelas - pCluster2.rKelas)**2) + ((jarak2.rLab - pCluster2.rLab)**2) +((jarak2.rPerpus - pCluster2.rPerpus)**2) + ((jarak2.rasioPDRB - pCluster2.rasioPDRB)**2) + ((jarak2.rasioGRB - pCluster2.rasioGRB)**2))
                jarakCluster2.append({'namaSekolah' : nama2, 'X1' : jarak2.guru, 'X2' : jarak2.rKelas,'X3' : jarak2.rLab,'X4' : jarak2.rPerpus,'X5' : jarak2.rasioPDRB,'X6' : jarak2.rasioGRB, 'jarak' : jaraknya2, 'kelompok' : 0})

            def myFunc(e):
                return e['jarak']

            jarakCluster1.sort(key=myFunc)
            jarakCluster2.sort(key=myFunc)

            for terdekat in dataAwal:
                if terdekat.namaSekolah == jarakCluster1[1]['namaSekolah']:
                    pCluster1 = terdekat

                if terdekat.namaSekolah == jarakCluster2[1]['namaSekolah']:
                    pCluster2 = terdekat
                
            cluster1 = {'X1' : pCluster1.guru,'X2' : pCluster1.rKelas,'X3' : pCluster1.rLab,'X4' : pCluster1.rPerpus,'X5' : pCluster1.rasioPDRB,'X6' : pCluster1.rasioGRB,}
            cluster2 = {'X1' : pCluster2.guru,'X2' : pCluster2.rKelas,'X3' : pCluster2.rLab,'X4' : pCluster2.rPerpus,'X5' : pCluster2.rasioPDRB,'X6' : pCluster2.rasioGRB,}
            # pprint(cluster1['X1'])
            
            c_cluster1Awal = 0
            c_cluster2Awal = 0
            c_cluster1Akhir = 1
            c_cluster2Akhir = 1

            while True:
                if c_cluster1Awal == c_cluster1Akhir and c_cluster2Awal == c_cluster2Akhir: 
                    break
                
                def cmp(a, b):
                    return (a > b) - (a < b)

                jarakCluster1.clear()
                jarakCluster2.clear()

                c1 = 0
                c2 = 0

                for jarak1 in dataAwal:
                    nama1 = jarak1.namaSekolah
                    jaraknya1 = math.sqrt((((jarak1.guru - cluster1['X1'])**2) + ((jarak1.rKelas - cluster1['X2'])**2) + ((jarak1.rLab - cluster1['X3'])**2) +((jarak1.rPerpus - cluster1['X4'])**2) + ((jarak1.rasioPDRB - cluster1['X5'])**2) + ((jarak1.rasioGRB - cluster1['X6'])**2)))
                    jarakCluster1.append({'namaSekolah' : nama1, 'X1' : jarak1.guru, 'X2' : jarak1.rKelas,'X3' : jarak1.rLab,'X4' : jarak1.rPerpus,'X5' : jarak1.rasioPDRB,'X6' : jarak1.rasioGRB, 'jarak' : jaraknya1, 'kelompok' : 0})

                for jarak2 in dataAwal:
                    nama2 = jarak2.namaSekolah
                    jaraknya2 = math.sqrt((((jarak2.guru - cluster2['X1'])**2) + ((jarak2.rKelas - cluster2['X2'])**2) + ((jarak2.rLab - cluster2['X3'])**2) +((jarak2.rPerpus - cluster2['X4'])**2) + ((jarak2.rasioPDRB - cluster2['X5'])**2) + ((jarak2.rasioGRB - cluster2['X6'])**2)))
                    jarakCluster2.append({'namaSekolah' : nama2, 'X1' : jarak2.guru, 'X2' : jarak2.rKelas,'X3' : jarak2.rLab,'X4' : jarak2.rPerpus,'X5' : jarak2.rasioPDRB,'X6' : jarak2.rasioGRB, 'jarak' : jaraknya2, 'kelompok' : 0})

                # pprint(jarakCluster1)
                # pprint(jarakCluster2)

                for n in range(len(jarakCluster1)):
                    a = cmp(jarakCluster1[n]['jarak'], jarakCluster2[n]['jarak'])
                    
                    if a == -1:
                        jarakCluster1[n]['kelompok'] = 1
                    elif a == 1:
                        jarakCluster1[n]['kelompok'] = 2
                    elif a == 0:
                        jarakCluster1[n]['kelompok'] = 0
                
                for n in range(len(jarakCluster2)):
                    a = cmp(jarakCluster2[n]['jarak'], jarakCluster1[n]['jarak'])
                    if a == -1:
                        jarakCluster2[n]['kelompok'] = 2
                    elif a == 1:
                        jarakCluster2[n]['kelompok'] = 1
                    elif a == 0:
                        jarakCluster2[n]['kelompok'] = 0

                for x in range(len(jarakCluster1)):
                    if jarakCluster1[x]['kelompok'] == 1:
                        c1 += 1
                    elif jarakCluster1[x]['kelompok'] == 2:
                        c2 += 1
                
                pprint(jarakCluster1)
                pprint(jarakCluster2)

                pusatbaru_c1 = []
                ex1_c1 = 0
                ex2_c1 = 0
                ex3_c1 = 0
                ex4_c1 = 0
                ex5_c1 = 0
                ex6_c1 = 0

                pusatbaru_c2 = []
                ex1_c2 = 0
                ex2_c2 = 0
                ex3_c2 = 0
                ex4_c2 = 0
                ex5_c2 = 0
                ex6_c2 = 0

                for data in jarakCluster1:
                    if data['kelompok'] == 1:
                        ex1_c1 += data['X1']
                        ex2_c1 += data['X2']
                        ex3_c1 += data['X3']
                        ex4_c1 += data['X4']
                        ex5_c1 += data['X5']
                        ex6_c1 += data['X6']

                    elif data['kelompok'] == 2:
                        ex1_c2 += data['X1']
                        ex2_c2 += data['X2']
                        ex3_c2 += data['X3']
                        ex4_c2 += data['X4']
                        ex5_c2 += data['X5']
                        ex6_c2 += data['X6']
            
                cluster1 = {'X1' : ex1_c1/c1,'X2' : ex2_c1/c1,'X3' : ex3_c1/c1,'X4' : ex4_c1/c1,'X5' : ex5_c1/c1,'X6' : ex6_c1/c1,}

                cluster2 = {'X1' : ex1_c2/c2,'X2' : ex2_c2/c2,'X3' : ex3_c2/c2,'X4' : ex4_c2/c2,'X5' : ex5_c2/c2,'X6' : ex6_c2/c2,}
                
                # pprint(cluster1)
                # pprint(cluster2)

                c_cluster1Awal = c_cluster1Akhir
                c_cluster2Awal = c_cluster2Akhir
                c_cluster1Akhir = c1
                c_cluster2Akhir = c2
            
            

            for datas in jarakCluster1:
                if datas['kelompok'] == 1:
                    anggotaC1.append(datas)
                elif datas['kelompok'] == 2:
                    anggotaC2.append(datas)

            # MOORA

            # menentukan bobot
            bc1 = 0.25 #guru
            bc2 = 0.2 #r.kelas
            bc3 = 0.2 #r.lab
            bc4 = 0.2 #r.perpus
            bc5 = 0.15 #rasio pd:rb
            bc6 = 0.25 #rasio guru:rb

            normalized1 = []
            normalized2 = []

            sqrtC1 = 0
            sqrtC2 = 0
            sqrtC3 = 0
            sqrtC4 = 0
            sqrtC5 = 0
            sqrtC6 = 0

            sqrtC1_2 = 0
            sqrtC2_2 = 0
            sqrtC3_2 = 0
            sqrtC4_2 = 0
            sqrtC5_2 = 0
            sqrtC6_2 = 0

            for datas in anggotaC1:
                sqrtC1 += datas['X1']**2
                sqrtC2 += datas['X2']**2
                sqrtC3 += datas['X3']**2
                sqrtC4 += datas['X4']**2
                sqrtC5 += datas['X5']**2
                sqrtC6 += datas['X6']**2
            
            for datas in anggotaC2:
                sqrtC1_2 += datas['X1']**2
                sqrtC2_2 += datas['X2']**2
                sqrtC3_2 += datas['X3']**2
                sqrtC4_2 += datas['X4']**2
                sqrtC5_2 += datas['X5']**2
                sqrtC6_2 += datas['X6']**2

            for dataku in anggotaC1:
                c1 = dataku['X1'] / math.sqrt(sqrtC1)
                c2 = dataku['X2'] / math.sqrt(sqrtC2)
                c3 = dataku['X3'] / math.sqrt(sqrtC3)
                c4 = dataku['X4'] / math.sqrt(sqrtC4)
                c5 = dataku['X5'] / math.sqrt(sqrtC5)
                c6 = dataku['X6'] / math.sqrt(sqrtC6)

                alternatif = {'namaSekolah' : dataku['namaSekolah'], 'C1' : c1,'C2' : c2,'C3' : c3,'C4' : c4,'C5' : c5,'C6' : c6,'X1' : dataku['X1'],'X2' : dataku['X2'],'X3' : dataku['X3'],'X4' : dataku['X4'],'X5' : dataku['X5'],'X6' : dataku['X6'],}
                normalized1.append(alternatif)

            for dataku in anggotaC2:
                c1_2 = dataku['X1'] / math.sqrt(sqrtC1_2)
                c2_2 = dataku['X2'] / math.sqrt(sqrtC2_2)
                c3_2 = dataku['X3'] / math.sqrt(sqrtC3_2)
                c4_2 = dataku['X4'] / math.sqrt(sqrtC4_2)
                c5_2 = dataku['X5'] / math.sqrt(sqrtC5_2)
                c6_2 = dataku['X6'] / math.sqrt(sqrtC6_2)

                alternatif2 = {'namaSekolah' : dataku['namaSekolah'], 'C1' : c1_2,'C2' : c2_2,'C3' : c3_2,'C4' : c4_2,'C5' : c5_2,'C6' : c6_2,'X1' : dataku['X1'],'X2' : dataku['X2'],'X3' : dataku['X3'],'X4' : dataku['X4'],'X5' : dataku['X5'],'X6' : dataku['X6'],}
                normalized2.append(alternatif2)

            for data in normalized1:
                c1 = data['C1'] * bc1
                c2 = data['C2'] * bc2
                c3 = data['C3'] * bc3
                c4 = data['C4'] * bc4
                c5 = data['C5'] * bc5
                c6 = data['C6'] * bc6

                alternatif = {'namaSekolah' : data['namaSekolah'], 'C1' : c1,'C2' : c2,'C3' : c3,'C4' : c4,'C5' : c5,'C6' : c6,'X1' : data['X1'],'X2' : data['X2'],'X3' : data['X3'],'X4' : data['X4'],'X5' : data['X5'],'X6' : data['X6'],}
                terbobot1.append(alternatif)
            
            for data in normalized2:
                c1_2 = data['C1'] * bc1
                c2_2 = data['C2'] * bc2
                c3_2 = data['C3'] * bc3
                c4_2 = data['C4'] * bc4
                c5_2 = data['C5'] * bc5
                c6_2 = data['C6'] * bc6

                alternatif2 = {'namaSekolah' : data['namaSekolah'], 'C1' : c1_2,'C2' : c2_2,'C3' : c3_2,'C4' : c4_2,'C5' : c5_2,'C6' : c6_2,'X1' : data['X1'],'X2' : data['X2'],'X3' : data['X3'],'X4' : data['X4'],'X5' : data['X5'],'X6' : data['X6'],}
                terbobot2.append(alternatif2)

            for data in terbobot1:
                dMax = data['C1'] + data['C2'] + data['C3'] + data['C4'] + data['C6']
                dMin = data['C5']

                Yi = dMax - dMin
                data['Yi'] = Yi
            
            for data in terbobot2:
                dMax = data['C1'] + data['C2'] + data['C3'] + data['C4'] + data['C6']
                dMin = data['C5']

                Yi = dMax - dMin
                data['Yi'] = Yi
            
            def myFun(e):
                return e['Yi']

            terbobot1.sort(key=myFun)
            terbobot2.sort(key=myFun)

            for datanya in terbobot1:
                final1.append(datanya)

            for datanya in terbobot2:
                final2.append(datanya)

            pprint(final2)
            
        # if dataForm.is_valid():
    
        # valueX = kecForm.cleaned_data.get('pilihKecamatan')
            # return values
            # return HttpResponseRedirect('data-sekolah')
    else:
        kecForm = KecamatanForm()
        bpForm = BPForm()

    contex = {
        'kecForm' : kecForm,
        'bpForm' : bpForm,
        'dataAwal' : dataAwal,
        'final1' : final1,
        'final2' : final2,
        }

    return render(request, 'mainapp/klasterisasi.html', contex)
    

    

# def dataklaster(request):
#     from .models import Post
#     hasil = request.POST.get('pilihKecamatan')

#     return HttpResponseRedirect(reverse('klasterisasi'))




# def cobaAjax(request):
#     if request.method == "GET":
#         get_value = request.GET['dikirim']
#         # terpilih = request.POST.get('pilihKecamatan')
#         context = {
#             'isi' : get_value
#         }
#         data = json.dumps(context, sort_keys=True)
#         return HttpResponse(data, content_type="application/json")

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['namaSekolah',
                'npsn',
                'bp',
                'status',
                'lastSync',
                'jumlahSync',
                'pd',
                'rombel',
                'guru',
                'pegawai',
                'rKelas',
                'rLab',
                'rPerpus'
                'rasioPDRB',
                'rasioGRB',
                'pilihKecamatan']

def dataSekolah_u(request):
    context = {
        'posts': Post.objects.all(),
        'posts': Post.objects.order_by('-lastSync'),
    }
    return render(request, 'mainapp/data_sekolah_u.html', context)

def dataSekolah(request):

    global valueX

    if request.method == 'POST':
        kecForm = KecamatanForm(request.POST)
        dataForm = DataForm(request.POST)
        if dataForm.is_valid():
            dataForm.save()
            return redirect('/datasekolah')
                
        # valueX = kecForm.cleaned_data.get('pilihKecamatan')
            # return values
            # return HttpResponseRedirect('data-sekolah')
    else:
        kecForm = KecamatanForm()
        dataForm = DataForm()
        
    context = {
        'posts': Post.objects.all(),
        'posts': Post.objects.order_by('-lastSync'),
        'kecForm' : kecForm,
        'dataForm' : dataForm
    }
    return render(request, 'mainapp/data_sekolah.html', context)

def updateDataForm(request, pk):

    item = Post.objects.get(id=pk)
    updater = DataForm(instance=item)
    
    if request.method == 'POST':
        updater = DataForm(request.POST, instance=item)
        if updater.is_valid():
            updater.save()
            return redirect('/datasekolah')
    else:
        updater = DataForm()

    context = {'updater' : updater}

    return render(request, context)

class PostDetailView(DetailView):
    model = Post

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['namaSekolah',
                'npsn',
                'bp',
                'status',
                'lastSync',
                'jumlahSync',
                'pd',
                'rombel',
                'guru',
                'pegawai',
                'rKelas',
                'rLab',
                'rPerpus',
                'rasioPDRB',
                'rasioGRB',
                'pilihKecamatan']

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/datasekolah'

# class UploadView(FormView):
#     template_name = 'mainapp/upload1.html'
#     form_class = UploadForm
#     success_url = '/datasekolah'

#     def form_valid(self, form):
#         form.process_data()
#         return super().form_valid(form), HttpResponse(render_to_string('mainapp/upload1.html'))

def upload_csv(request):
    from .models import Post
    global valueX
    cPD = 0
    cG = 0
    cRombel = 0
    
    data = {}
    if "GET" == request.method:
        return render(request, 'mainapp/data_sekolah.html', data)
    # if not GET, then proceed
    try:
        csv_file = request.FILES["csv_file"]
        if not csv_file.name.endswith('.csv'):
            messages.error(request,'File is not CSV type')
            return HttpResponseRedirect(reverse('data-sekolah'))
        #if file is too large, return
        if csv_file.multiple_chunks():
            messages.error(request,"Uploaded file is too big (%.2f MB)." % (csv_file.size/(1000*1000),))
            return HttpResponseRedirect(reverse('data-sekolah'))
        
        file_data = csv_file.read().decode("utf-8")
        
        lines = file_data.split("\n")
		#loop over the lines and save them in db. If error , store as string and then display
        for line in lines:
            fields = line.split(";")
            result = request.POST.get('pilihKecamatan')
            try:
                form = Post()
                form.namaSekolah = fields[1]
                form.npsn = fields[2]
                form.bp = fields[3]
                form.status = fields[4]
                form.lastSync = datetime.datetime.now()
                form.pd = int(fields[7])
                form.rombel = int(fields[8])
                form.guru = int(fields[9])
                form.pegawai = int(fields[10])
                form.rKelas = int(fields[11])
                form.rLab = int(fields[12])
                form.rPerpus = int(fields[13])
                cPD = int(fields[7])
                cRombel = int(fields[8])
                cG = int(fields[9])
                form.rasioPDRB = cPD/cRombel
                form.rasioGRB = cG/cRombel
                form.pilihKecamatan = result
                # form.namaSekolah = fields[1]
                form.save()
                # result = request.POST.get('pilihKecamatan')
                # print(result)
                
            except Exception as e:
                logging.getLogger("error_logger").error(repr(e))
                pass
    
    except Exception as e:
        logging.getLogger("error_logger").error("Unable to upload file. "+repr(e))
        messages.error(request,"Unable to upload file. "+repr(e))
    
    
    return HttpResponseRedirect(reverse('data-sekolah'))