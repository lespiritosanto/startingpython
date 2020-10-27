m = float(input('Digite a metragem: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000

print('''A metragem convertida fica: 
km: {:.2f} km, 
hm: {:.2f} hm, 
dam: {:.2f} dam
dm: {:.2f} dm, 
cm: {:.2f} cm, 
mm: {:.2f} mm.'''
      .format(km, hm, dam, dm, cm, mm))
