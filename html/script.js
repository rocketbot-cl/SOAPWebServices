function addOptions(serviceNames) {
    var select = document.getElementById("serviceNames")
    for (serviceName of serviceNames) {
        var opt = document.createElement('option');
        opt.value = serviceName;
        opt.innerHTML = serviceName;
        select.appendChild(opt);
        if (serviceName.toLowerCase() == document.serviceNames_serviceName) {
            opt.selected = true
        }
    }

}

data = getDataFromRB({module_name:"SOAPWebServices", command_name:"getMethods"})
.then(data => {

    console.log(data["serviceNames"])
    data = data.replaceAll("'", "\"")
    data = JSON.parse(`${data}`)
    data["serviceNames"].push("---- Select Option ----")
    serviceNames = data["serviceNames"]
    serviceNames.reverse()
    addOptions(serviceNames)

})

