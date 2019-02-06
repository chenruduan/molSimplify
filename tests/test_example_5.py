import helperFuncs as hp

def test_example_5(tmpdir):
    testName="example_5"
    threshMLBL = 0.1
    threshLG =  1.0
    threshOG = 2.0
    [passNumAtoms,passMLBL,passLG,passOG,pass_report,pass_qcin] = hp.runtest(tmpdir,testName,threshMLBL,threshLG,threshOG)
    assert passNumAtoms
    assert passMLBL
    assert passLG
    assert passOG
    assert pass_report,pass_qcin

def test_example_5_No_FF(tmpdir):
    testName="example_5"
    threshMLBL = 0.1
    threshLG =  1.0
    threshOG = 2.0
    [passNumAtoms,passMLBL,passLG,passOG,pass_report,pass_qcin] = hp.runtestNoFF(tmpdir,testName,threshMLBL,threshLG,threshOG)
    assert passMLBL
    assert passLG
    assert passOG
    assert pass_report,pass_qcin
