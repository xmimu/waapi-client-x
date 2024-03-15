#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@File:        client.py
@Author:      lgx
@Contact:     1101588023@qq.com
@Time:        2024/01/31 11:34
@Description:
"""

from typing import Literal
from waapi import WaapiClient
from waapix.constants.uri import *
from waapix.data_class import *


class SoundEngineClient(WaapiClient):

    # region Sound Engine Method

    def engine_execute_action_on_event(self):
        pass

    def engine_get_state(self):
        pass

    def engine_get_switch(self):
        pass

    def engine_post_event(self):
        pass

    def engine_post_msg_monitor(self):
        pass

    def engine_post_trigger(self):
        pass

    def engine_register_game_obj(self):
        pass

    def engine_reset_rtpc_value(self):
        pass

    def engine_seek_on_event(self):
        pass

    def engine_set_default_listeners(self):
        pass

    def engine_setGameObjectAuxSendValues(self):
        pass

    def engine_setGameObjectOutputBusVolume(self):
        pass

    def engine_set_listeners(self):
        pass

    def engine_setListenerSpatialization(self):
        pass

    def engine_setMultiplePositions(self):
        pass

    def engine_setObjectObstructionAndOcclusion(self):
        pass

    def engine_set_position(self):
        pass

    def engine_set_rtpc_value(self):
        pass

    def engine_set_scaling_factor(self):
        pass

    def engine_set_state(self):
        pass

    def engine_set_switch(self):
        pass

    def engine_stop_all(self):
        pass

    def engine_stop_playing_id(self):
        pass

    def engine_unregister_game_obj(self):
        pass

    # endregion


class WwiseCoreClient(WaapiClient):

    # region Core Method
    def undo_begin_group(self) -> None:
        self.call(ak_wwise_core_undo_beginGroup)

    def undo_cancel_group(self, undo: bool = False) -> None:
        self.call(ak_wwise_core_undo_cancelGroup, {'undo': undo})

    def undo_end_group(self, name) -> None:
        self.call(ak_wwise_core_undo_endGroup, {'displayName': name})

    def undo(self) -> None:
        self.call(ak_wwise_core_undo_undo)

    def transport_create(self, t_obj: TransportObject) -> int:
        """
        针对给定 Wwise 对象创建走带对象。可使用返回的走带对象来播放、停止、暂停和继续播放 Wwise 对象（通过另一走带函数实现）。
        :param w_obj: Wwise 对象
        :param g_obj:
        :return: { 'transport': transport_id }
        """
        return self.call(ak_wwise_core_transport_create, t_obj.as_args())['transport']

    def transport_destroy(self, transport_id: int) -> None:
        self.call(ak_wwise_core_transport_destroy, {'transport': transport_id})

    def transport_execute_action(self, action: TransportAction, transport_id: int | None = None):
        """
        针对给定走带对象或所有走带对象（如未作任何指定）执行某项动作。
        :param action: play, pause, stop...
        :param transport_id:
        :return:
        """
        self.call(ak_wwise_core_transport_executeAction, {'transport': transport_id, 'action': action.value})

    def transport_get_list(self) -> list[TransportObject]:
        data = []
        for i in self.call(ak_wwise_core_transport_getList)['list']:
            obj = TransportObject(i['object'], i['gameObject'], i['transport'])
            data.append(obj)
        return data

    def transport_get_state(self, transport_id: int) -> TransportState:
        result = self.call(ak_wwise_core_transport_getState, {'transport': transport_id})
        return TransportState(result['state'])

    def transport_prepare(self, w_obj: str) -> None:
        self.call(ak_wwise_core_transport_prepare, {'object': w_obj})

    def switch_add_assignment(self, child_obj: str, state_obj: str) -> None:
        self.call(ak_wwise_core_switchContainer_addAssignment,
                  {'child': child_obj, 'stateOrSwitch': state_obj})

    def switch_get_assignment(self, w_obj: str) -> None:
        self.call(ak_wwise_core_switchContainer_getAssignments, {'id': w_obj})

    def switch_remove_assignment(self, child_obj: str, state_obj: str) -> None:
        '''移除的对象须为 Switch Container 的子对象且当前指派给了 State。'''
        self.call(ak_wwise_core_switchContainer_removeAssignment,
                  {'child': child_obj, 'stateOrSwitch': state_obj})

    def bank_convert_external_sources(self):
        pass

    def bank_generate(self):
        pass

    def bank_get_inclusions(self, w_obj: str) -> list:
        result = self.call(ak_wwise_core_soundbank_getInclusions, {'soundbank': w_obj})
        if result and 'inclusions' in result:
            return result['inclusions']
        return []

    def bank_set_inclusions(self, w_obj: str, inclusions: list,
                            operation: Literal['add', 'remove', 'replace'] = 'add') -> None:
        self.call(ak_wwise_core_soundbank_setInclusions,
                  {'soundbank': w_obj, 'operation': operation, 'inclusions': inclusions})

    def bank_process_definition_files(self):
        pass

    def sound_set_activate_source(self):
        pass

    def remote_connect(self):
        pass

    def remote_disconnect(self):
        pass

    def remote_get_available_consoles(self):
        pass

    def remote_get_connection_status(self):
        pass

    def project_save(self):
        pass

    def profiler_enable_profiler_data(self):
        pass

    def profiler_get_audio_objects(self):
        pass

    def profiler_get_busses(self):
        pass

    def profiler_get_cursor_time(self):
        pass

    def profiler_get_game_objects(self):
        pass

    def profiler_get_rtpcs(self):
        pass

    def profiler_get_voice_contributions(self):
        pass

    def profiler_get_voices(self):
        pass

    def profiler_start_capture(self):
        pass

    def profiler_stop_capture(self):
        pass

    def plugin_get_list(self):
        pass

    def plugin_get_properties(self):
        pass

    def plugin_get_property(self):
        pass

    def object_copy(self):
        pass

    def object_create(self):
        pass

    def object_delete(self):
        pass

    def object_diff(self):
        pass

    def object_get(self):
        pass

    def object_get_attenuation_curve(self):
        pass

    def object_get_property_and_reference_names(self):
        pass

    def object_get_property_info(self):
        pass

    def object_get_property_names(self):
        pass

    def object_get_types(self) -> list:
        return self.call(ak_wwise_core_object_getTypes)['return']

    def object_is_property_enabled(self):
        pass

    def object_move(self):
        pass

    def object_paste_properties(self):
        pass

    def object_set(self):
        pass

    def object_set_attenuation_curve(self):
        pass

    def object_set_name(self):
        pass

    def object_set_notes(self):
        pass

    def object_set_property(self):
        pass

    def object_set_randomizer(self):
        pass

    def object_set_reference(self):
        pass

    def get_log(self):
        pass

    def get_project_info(self):
        pass

    def get_info(self):
        pass

    def audio_import(self):
        pass

    def audio_import_tab_delimited(self):
        pass

    def audio_getMinMaxPeaksInRegion(self):
        pass

    def audio_getMinMaxPeaksInTrimmedRegion(self):
        pass

    # endregion


class UIClient(WaapiClient):

    # region UI Method

    def ui_execute_command(self, command: str,
                           objects: list | None = None,
                           platforms: list | None = None) -> None:
        self.call(ak_wwise_ui_commands_execute, {
            'command': command,
            'objects': objects if objects else [],
            'platforms': platforms if platforms else []
        })

    def ui_get_commands(self) -> list:
        return self.call(ak_wwise_ui_commands_getCommands)['commands']

    def ui_register_commands(self, commands: list[dict]) -> None:
        """
        注册命令到 Wwise 设计软件中，这里的 command_id 是 str 类型
        更多参数参考：https://www.audiokinetic.com/zh/library/2022.1.9_8365/?source=SDK&id=ak_wwise_ui_commands_register.html
        :param commands: [ {'id': id, 'displayName': display_name} ]
        :return:
        """
        self.call(ak_wwise_ui_commands_register, commands)

    def ui_unregister_commands(self, commands: list[str]) -> None:
        """
        移除在 Wwise 中注册的命令，这里的 command_id 是 str 类型
        :param commands: [command_id]
        :return:
        """
        self.call(ak_wwise_ui_commands_unregister, commands)

    def ui_get_selected_objects(self, options: list | None = None) -> list:
        """
        获取在 Wwise 中选中的一系列对象，默认返回 [id, name]
        详细返回选项参考：https://www.audiokinetic.com/zh/library/2022.1.9_8365/?source=SDK&id=ak_wwise_ui_getselectedobjects.html
        :param options: [ {'return': ['id', 'name', 'type', 'notes'...]} ]
        :return:
        """
        if options is None: options = ['id', 'name', 'notes', 'type', 'path']
        result = self.call(ak_wwise_ui_getSelectedObjects, options={'return': options})
        if result and result['objects']:
            return result['objects']
        else:
            return []

    def ui_close_project(self, bypass_save: bool = False) -> bool:
        return self.call(ak_wwise_ui_project_close, {'bypassSave': bypass_save}) and True

    def ui_open_project(self, path: str, on_upgrade='migrate', bypass_save=False) -> None:
        self.call(ak_wwise_ui_project_open, {
            'path': path,
            'onUpgrade': on_upgrade,
            'bypassSave': bypass_save
        })

    # endregion
