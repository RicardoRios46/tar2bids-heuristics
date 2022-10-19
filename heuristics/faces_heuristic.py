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

    faces = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-faces_run-{item:02d}_bold')
    localizer = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-localizer_run-{item:02d}_bold')
    depth = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-DepthLoc_run-{item:02d}_bold')
    fopsr = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-FOPSRLoc_run-{item:02d}_bold')
    

    info[faces]=[]
    info[localizer]=[]
    info[depth]=[]
    info[fopsr]=[]

    for idx, s in enumerate(seqinfo):
       
        if ('FACES' in (s.series_description).strip()) and (s.dim4>1):
            info[faces].append({'item': s.series_id})
                    
        elif ('localizer' in (s.series_description).strip()) and (s.dim4>1):
            if ('depth' in (s.series_description).strip()):
                info[depth].append({'item': s.series_id})
            elif ('FOPSR' in (s.series_description).strip()):
                info[fopsr].append({'item': s.series_id})
            else:
                info[localizer].append({'item': s.series_id})            
        

    return info
