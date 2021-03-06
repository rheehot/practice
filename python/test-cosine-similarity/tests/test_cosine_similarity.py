# -*- coding: utf8 -*-
from cosine_similarity import *

def test_cosine_similarity():
    v1 = { '최순실': 0.0, '청사': 0.301029995664, '대검': 0.47712125472, '포클레인': 0.301029995664, '돌진': 0.301029995664, '운전자': 0.778151250384 }
    v2 = { '포클레인': 0.301029995664, '최순실': 0.0, '남성': 0.778151250384, '돌진': 0.301029995664, '대검찰청': 0.301029995664 }
    assert abs(0.184065001513 - cosine_similarity(v1, v2, 1.0511999025148653, 0.9366838011527675)) < 0.00000001
