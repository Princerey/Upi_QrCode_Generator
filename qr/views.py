from django.shortcuts import render
import qrcode
import qrcode.image.svg
from io import BytesIO

def index(request):
    context = {}
    if request.method == "POST":
        factory = qrcode.image.svg.SvgImage
        img = qrcode.make("upi://pay?pa="+request.POST.get("qr_text","")+"&pn=.", image_factory=factory, box_size=20)
        stream = BytesIO()
        img.save(stream)
        context["svg"] = stream.getvalue().decode()

    return render(request, "homepage.html", context=context)