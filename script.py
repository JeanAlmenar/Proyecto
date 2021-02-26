import me
def upsPullTrkService = ctx.getBean('upsPullTrkService'):
    print("ok", ctx.getBean)
def s = Shipment.get(27528954729)
def tn = s.trackingNumber
def trackingData = upsPullTrkService.getTrkEvents([tn])
trackingData.each { td ->
println "------------------------------------------------"
println "${td.sucursal} - ${td.eventDate} - ${td.description}"
}
"Done"