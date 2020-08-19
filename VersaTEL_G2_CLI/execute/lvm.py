# coding=utf-8
import consts
import sundry as s
import sys

class LVM():
    def __init__(self):
        self.logger = consts.glo_log()
        self.data_vg = self.get_vg()
        self.data_lv = self.get_thinlv()

    def get_vg(self):
        cmd = 'vgs'
        result = s.get_cmd_result(sys._getframe().f_code.co_name, cmd, s.create_oprt_id())
        return result

    def get_thinlv(self):
        cmd = 'lvs'
        result = s.get_cmd_result(sys._getframe().f_code.co_name, cmd, s.create_oprt_id())
        return result

    def refine_thinlv(self):
        all_lv = self.data_vg.splitlines()
        list_thinlv = []
        re_ = '\s*(\S*)\s*(\S*)\s*\S*\s*(\S*)\s*\S*\s*\S*\s*\S*\s*?'
        for one in all_lv:
            if 'twi' in one:
                thinlv_one = s.re_findall(re_,one)
                list_thinlv.append(list(thinlv_one[0]))
        return list_thinlv

    def refine_vg(self):
        all_vg = self.data_lv.splitlines()
        list_vg = []
        re_ = '\s*(\S*)\s*\S*\s*\S*\s*\S*\s*\S*\s*(\S*)\s*(\S*)\s*?'
        for one in all_vg[1:]:
            vg_one = s.re_findall(re_,one)
            list_vg.append(list(vg_one[0]))
        return list_vg

    def is_vg_exists(self,vg):
        if vg in self.data_vg:
            return True

    def is_thinlv_exists(self,thinlv):
        all_lv_list = self.data_lv.splitlines()[1:]
        for one in all_lv_list:
            if 'twi' and thinlv in one:
                return True