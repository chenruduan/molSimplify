import helperFuncs as hp

def test_molcas_casscf(tmpdir):
    testName="molcas_casscf"
    threshMLBL = 0.1
    threshLG =  1.0
    threshOG = 2.0
    [passNumAtoms,passMLBL,passLG,passOG,pass_report,pass_qcin] = hp.runtest(tmpdir,testName,threshMLBL,threshLG,threshOG)
    assert passNumAtoms
    assert passMLBL
    assert passLG
    assert passOG
    assert pass_report
