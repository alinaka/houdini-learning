import json


def set_AOVs(mantra):
    config = json.loads("aovs_config.json")
    aovs = config["extraImagePlanes"]
    num_aux = len(aovs)
    extraImagePlanes = mantra.parm("vm_numaux")
    extraImagePlanes.set(num_aux)

    for i, setting in enumerate(aovs):
        vex_variable = mantra.parm("vm_variable_plane{}".format(i))
        vex_variable.set(setting["variable"])
        vex_type = mantra.parm("vm_vextype_plane{}".format(i))
        vex_type.set(setting["vex_type"])
        channel = mantra.parm("vm_channel_plane{}".format(i))
        channel.set(setting["channel"])
        quantize = mantra.parm("vm_quantize_plane{}".format(i))
        quantize.set(setting["quantize"])
        sfilter = mantra.parm("vm_sfilter_plane{}".format(i))
        sfilter.set(setting["sfilter"])
        pfilter = mantra.parm("vm_pfilter_plane{}".format(i))
        pfilter.set(setting.get("pfilter", ""))
