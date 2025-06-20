m = float(input('Uma distância em metros: '))
km, hm, dam, dm, cm, mm = (m / 1000), (m / 100), (m / 10), (m * 10), (m * 100), (m * 1000)
print("""A medida de {}m corresponde a
{}km
{}hm
{}dam
{:.0f}dm
{:.0f}cm
{:.0f}mm""".format(m, km, hm, dam, dm, cm, mm))
