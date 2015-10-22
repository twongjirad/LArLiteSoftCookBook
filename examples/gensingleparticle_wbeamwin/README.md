contains example driver fcl files to generate single particle events.

some modifications have been made. 

for one, the default scintillation light yield has been changed to potentially better match operation at -70 kV.
also, the quantum efficiency of the tubes has been adjusted to match roughyl the data as well.

there is an important modification compared to typical single particle generation, which won't trigger the PMT beam window readout:
a new module, fakebnb, is used to insert a fake BNB gate.  the downstream modules, optfem, opadcsim, triggersim have been adjusted to use this fake bnb gate.

as of oct. 22, 2015, this module has been added to uboonecode/develop