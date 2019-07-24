import io
import pytest

from proces_range_log import *


@pytest.fixture()
def range_log():
    """Setup a file like object of the ranging service used for the testing functions."""
    file_content = io.StringIO("""\
No.;Port;Host Time;Event;Status;Raw Value;Raw Val. Mean;Raw Val. StdDev;Distance[m];Dist. Mean;Dist. StdDev
1;COM12;2019-07-20 20:27:11;Session Indication;Ok;FeiMaster:-717.844(000ffc70)   FeiSlave:692.656(00000370)  FeiFactor:-0.853   c:-0.591   RSSI:-110;;;;;
2;COM12;2019-07-20 20:27:18;RangingStatus;Ok;3350;3350.000;0.000;151.582;151.582;0.000
3;COM12;2019-07-20 20:27:19;Session Indication;Ok;FeiMaster:-591.906(000ffd10)   FeiSlave:617.094(00000310)  FeiFactor:-0.853   c:-0.526   RSSI:-110;;;;;
4;COM12;2019-07-20 20:27:26;RangingStatus;Ok;3327;3338.000;16.279;150.481;151.031;0.779
5;COM12;2019-07-20 20:27:27;Session Indication;Ok;FeiMaster:-642.281(000ffcd0)   FeiSlave:642.281(00000330)  FeiFactor:-0.853   c:-0.548   RSSI:-110;;;;;
6;COM12;2019-07-20 20:27:34;RangingStatus;Ok;3291;3322.000;29.749;148.880;150.314;1.359
7;COM12;2019-07-20 20:27:35;Session Indication;Ok;FeiMaster:-692.656(000ffc90)   FeiSlave:667.469(00000350)  FeiFactor:-0.853   c:-0.569   RSSI:-110;;;;;
8;COM12;2019-07-20 20:27:42;RangingStatus;Ok;3330;3324.000;24.563;150.659;150.400;1.123
9;COM12;2019-07-20 20:27:43;Session Indication;Ok;FeiMaster:-692.656(000ffc90)   FeiSlave:642.281(00000330)  FeiFactor:-0.853   c:-0.548   RSSI:-109;;;;;
10;COM12;2019-07-20 20:27:50;RangingStatus;Ok;3330;3325.000;21.418;150.638;150.448;0.978""")

    csv_row = csv.DictReader(file_content, delimiter=';')
    return csv_row


def test_get_timestamp_returns_string_time_into_numbers():
    assert get_timestamp("2019-07-20 20:27:11") == 1563647231.0
    assert get_timestamp("2019-07-20 20:27:21") == 1563647241.0
    assert get_timestamp("2019-07-20 21:27:21") == 1563650841.0

    assert get_timestamp("2019-07-20 21:27:21") - get_timestamp("2019-07-20 20:27:21") == 3600


def test_indication_info_generates_tuple_of_timestamp_and_raw_value(range_log):
    indication_info = generate_indication_info(source=range_log)

    assert next(indication_info) == (1563647231.0, 'FeiMaster:-717.844(000ffc70)   FeiSlave:692.656(00000370)  '
                                                   'FeiFactor:-0.853   c:-0.591   RSSI:-110')

    assert next(indication_info) == (1563647239.0, 'FeiMaster:-591.906(000ffd10)   FeiSlave:617.094(00000310)  '
                                                   'FeiFactor:-0.853   c:-0.526   RSSI:-110')

    assert next(indication_info) == (1563647247.0, 'FeiMaster:-642.281(000ffcd0)   FeiSlave:642.281(00000330)  '
                                                   'FeiFactor:-0.853   c:-0.548   RSSI:-110')