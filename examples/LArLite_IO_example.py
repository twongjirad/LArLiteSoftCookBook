import ROOT
from ROOT import *
import os
from array import array

input_directory = "ConsolidatedROOTfiles/"

outfile = ROOT.TFile("efficiency.root","recreate")
outtree = ROOT.TTree("efficiency_tree","efficiency_tree")

event_num = array('i',[0])
energy    = array('f',[0])
xpos      = array('f',[0])
num       = array('i',[0])
num1      = array('i',[0])
num2      = array('i',[0])
num3      = array('i',[0])
num5      = array('i',[0])
num10     = array('i',[0])
num15     = array('i',[0])
num20     = array('i',[0])
num25     = array('i',[0])
num30     = array('i',[0])
num40     = array('i',[0])
num50     = array('i',[0])

outtree.Branch('event_id', event_num , 'event_id/I')
outtree.Branch('energy'  , energy    , 'energy/F'  )
outtree.Branch('xpos'    , xpos      , 'xpos/F'    )
outtree.Branch('n'       , num       , 'n/I'       )
outtree.Branch('n1'      , num1      , 'n1/I'      )
outtree.Branch('n2'      , num2      , 'n2/I'      )
outtree.Branch('n3'      , num3      , 'n3/I'      )
outtree.Branch('n5'      , num5      , 'n5/I'      )
outtree.Branch('n10'     , num10     , 'n10/I'     )
outtree.Branch('n15'     , num15     , 'n15/I'     )
outtree.Branch('n20'     , num20     , 'n20/I'     )
outtree.Branch('n25'     , num25     , 'n25/I'     )
outtree.Branch('n30'     , num30     , 'n30/I'     )
outtree.Branch('n40'     , num40     , 'n40/I'     )
outtree.Branch('n50'     , num50     , 'n50/I'     )


tick = 1
for subdir in os.listdir(input_directory):

    mc_info_infile         = "%s/%s/larlite_mcinfo.root" %(input_directory,subdir)
    mc_opflash_info_infile = "%s/%s/larlite_opdata.root" %(input_directory,subdir)

    manager = larlite.storage_manager()
    manager.set_io_mode(manager.kREAD)
    manager.add_in_filename(mc_opflash_info_infile)
    manager.set_in_rootdir("")
    manager.open()
    
    ndict   = {}
    n1dict  = {}
    n2dict  = {}
    n3dict  = {}
    n5dict  = {}
    n10dict = {}
    n15dict = {}
    n20dict = {}
    n25dict = {}
    n30dict = {}
    n40dict = {}
    n50dict = {}

    while manager.next_event():
	opflashdata = manager.get_data(larlite.data.kOpFlash,"opflash")

        n1  = 0
	n2  = 0
        n3  = 0
        n5  = 0
	n10 = 0
        n15 = 0
        n20 = 0
        n25 = 0
        n30 = 0
        n40 = 0
	n50 = 0

        for n in xrange(opflashdata.size()):
            flash   = opflashdata.at(n)
            time    = flash.Time()
            if time > 15 or time < 0:
                continue

            tot_PE  = flash.TotalPE()

            if tot_PE >= 50:
                n1  += 1
                n2  += 1
		n3  += 1
                n5  += 1
                n10 += 1
		n15 += 1
                n20 += 1
                n25 += 1
                n30 += 1
                n40 += 1
                n50 += 1

            elif tot_PE >= 40:
                n1  += 1
                n2  += 1
                n3  += 1
	        n5  += 1
        	n10 += 1
                n15 += 1
                n20 += 1
                n25 += 1
                n30 += 1
                n40 += 1

            elif tot_PE >= 30:
                n1  += 1
                n2  += 1
        	n3  += 1
                n5  += 1
                n10 += 1
        	n15 += 1
                n20 += 1
                n25 += 1
                n30 += 1

            elif tot_PE >= 25:

                n1  += 1
                n2  += 1
                n3  += 1
                n5  += 1
                n10 += 1
                n15 += 1
                n20 += 1
        	n25 += 1

            elif tot_PE >= 20:

                n1  += 1
                n2  += 1
                n3  += 1
                n5  += 1
                n10 += 1
                n15 += 1
        	n20 += 1

            elif tot_PE >= 15:

                n1  += 1
                n2  += 1
                n3  += 1
                n5  += 1
                n10 += 1
		n15 += 1
                n20 += 1
                
            elif tot_PE >= 10:

                n1  += 1
        	n2  += 1
                n3  += 1
                n5  += 1
                n10 += 1

            elif tot_PE >= 5:

                n1  += 1
	        n2  += 1
                n3  += 1
                n5  += 1

	    elif tot_PE >= 3:

                n1  += 1
                n2  += 1
                n3  += 1

            elif tot_PE >= 2:

                n1 += 1
                n2 += 1

            elif tot_PE >= 1:

                n1 +=1

        evt_id = manager.event_id()

        ndict.update({evt_id:opflashdata.size()})
        n1dict.update({evt_id:n1})
        n2dict.update({evt_id:n2})
        n3dict.update({evt_id:n3})
        n5dict.update({evt_id:n5})
        n10dict.update({evt_id:n10})
        n15dict.update({evt_id:n15})
        n20dict.update({evt_id:n20})
        n25dict.update({evt_id:n25})
        n30dict.update({evt_id:n30})
        n40dict.update({evt_id:n40})
        n50dict.update({evt_id:n50})

    print tick
    tick +=1
    manager.close()

    manager = larlite.storage_manager()
    manager.set_io_mode(manager.kREAD)
    manager.add_in_filename(mc_info_infile)
    manager.set_in_rootdir("")
    manager.open()

    while manager.next_event():
        mcdata   = manager.get_data(larlite.data.kMCTruth,"generator")
        mct      = mcdata[0]
        mcp      = mct.GetParticles()[0]
        mcs      = mcp.Trajectory()[0]

        event_num[0] = mcdata.event_id()
        energy[0]    = mcs.E()
        xpos[0]      = mcs.X()
        num[0]       = ndict[mcdata.event_id()]
        num1[0]      = n1dict[mcdata.event_id()]
        num2[0]      = n2dict[mcdata.event_id()]
        num3[0]      = n3dict[mcdata.event_id()]
        num5[0]      = n5dict[mcdata.event_id()]
        num10[0]     = n10dict[mcdata.event_id()]
        num15[0]     = n15dict[mcdata.event_id()]
        num20[0]     = n20dict[mcdata.event_id()]
        num25[0]     = n25dict[mcdata.event_id()]
        num30[0]     = n30dict[mcdata.event_id()]
        num40[0]     = n40dict[mcdata.event_id()]
        num50[0]     = n50dict[mcdata.event_id()]

        outtree.Fill()

    manager.close()

outfile.Write()
