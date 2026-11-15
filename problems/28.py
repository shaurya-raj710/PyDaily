price = int(input())
quan = int(input())

sub = price*quan

gst = (sub*18//100)
total = sub + gst
print(f"Subtotal: {sub}, GST: {gst}, Total: {total}")