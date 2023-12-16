#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2023 pigeon-sable
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
vc_manager：Discord Bot として動作するプログラムです。
            指定のチャンネルに入室したとき、退出したときに通知を行います。
"""

__author__ = "pigeon-sable"
__version__ = "0.2.1"
__date__ = "2023/05/06 (Created: 2023/02/22)"

import datetime
import os
import sys

import discord
from dotenv import load_dotenv


def main():
    """
    Discord Botとして動作するメイン（main）プログラムです。
    """
    load_dotenv()

    client = discord.Client(intents=discord.Intents.default())

    room_id = {}

    @client.event
    async def on_ready():
        for channel in client.get_all_channels():
            if channel.name == "tech-meetup":
                room_id["VOICE_CHAT_ROOM_ID"] = channel.id
                print("---------------------------------")
                print("Channel Name: " + channel.name)
                print("Channel ID: " + str(channel.id))
                print("---------------------------------")
            elif channel.name == "lobby":
                room_id["NOTIFY_ROOM_ID"] = channel.id
                print("---------------------------------")
                print("Channel Name: " + channel.name)
                print("Channel ID: " + str(channel.id))
                print("---------------------------------")

    member_list = {}

    @client.event
    async def on_voice_state_update(member, before, after):
        if before.channel != after.channel:
            # 通知メッセージを書き込むテキストチャンネル
            notify_room = client.get_channel(room_id["NOTIFY_ROOM_ID"])

            # 入退室を監視する対象のボイスチャンネル
            voice_chat_room_id = room_id["VOICE_CHAT_ROOM_ID"]

            # 入室通知
            if after.channel is not None and after.channel.id == voice_chat_room_id:
                member_list[member.id] = datetime.datetime.now()
                await notify_room.send(
                    f"** {after.channel.name} ** に、__{member.name}__ が入室しました！"
                )

            # 退室通知
            if before.channel is not None and before.channel.id == voice_chat_room_id:
                await notify_room.send(
                    f"** {before.channel.name} ** から、__{member.name}__ が退出しました！"
                )
                await notify_room.send(
                    f"{(datetime.datetime.now() - member_list[member.id]).seconds // 60} 分間作業をしていました。お疲れ様でした。"
                )

    client.run(os.environ["ACCESS_TOKEN"])

    return 0


if __name__ == "__main__":
    sys.exit(main())
