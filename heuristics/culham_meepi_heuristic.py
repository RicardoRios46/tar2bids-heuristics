import os
import numpy
from cfmm_base import infotodict as cfmminfodict
from cfmm_base import create_key

def infotodict(seqinfo):
    """Heuristic evaluator for determining which runs belong where
    allowed template fields - follow python string module:
    item: index within category
    subject: participant id
    seqitem: run number during scanning
    subindex: sub index within group
    """

    # call cfmm for general labelling and get dictionary
    info = cfmminfodict(seqinfo)

    head = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-head_run-{item:02d}_bold')

    task = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-phantomArmMove_run-{item:02d}_bold')
    

    info[head]=[]
    info[task]=[]

    for idx, s in enumerate(seqinfo):
       
        if ('phantomArmMove' in (s.series_description).strip()) and (s.dim4>1):
            info[task].append({'item': s.series_id})          
        
        elif ('head' in (s.series_description).strip()) and (s.dim4>1):
            info[head].append({'item': s.series_id})


    return info
