class ProtocolInfo:

    # RakNet Offline Message ID:
    MAGIC: bytes = b"\x00\xff\xff\x00\xfe\xfe\xfe\xfe\xfd\xfd\xfd\xfd\x12\x34\x56\x78"

    # RakNet Packet IDs:
    ONLINE_PING: int = 0x00
    OFFLINE_PING: int = 0x01
    OFFLINE_PING_OPEN_CONNECTIONS: int = 0x02
    ONLINE_PONG: int = 0x03
    OPEN_CONNECTION_REQUEST_1: int = 0x05
    OPEN_CONNECTION_REPLY_1: int = 0x06
    OPEN_CONNECTION_REQUEST_2: int = 0x07
    OPEN_CONNECTION_REPLY_2: int = 0x08
    CONNECTION_REQUEST: int = 0x09
    CONNECTION_REQUEST_ACCEPTED: int = 0x10
    NEW_INCOMING_CONNECTION: int = 0x13
    DISCONNECT: int = 0x15
    INCOMPATIBLE_PROTOCOL_VERSION: int = 0x19
    OFFLINE_PONG: int = 0x1c
    FRAME_SET: int = 0x80
    NACK: int = 0xa0
    ACK: int = 0xc0

class GameProtocolInfo:

    # Minecraft's Game Packet IDs:
    LOGIN: int = 0x01
    PLAY_STATUS: int = 0x02
    SERVER_TO_CLIENT_HANDSHAKE: int = 0x03
    CLIENT_TO_SERVER_HANDSHAKE: int = 0x04
    DISCONNECT: int = 0x05
    RESOURCE_PACKS_INFO: int = 0x06
    RESOURCE_PACK_STACK: int = 0x07
    RESOURCE_PACK_CLIENT_RESPONSE: int = 0x08
    TEXT: int = 0x09
    SET_TIME: int = 0x0a
    START_GAME: int = 0x0b
    ADD_PLAYER: int = 0x0c
    ADD_ENTITY: int = 0x0d
    REMOVE_ENTITY: int = 0x0e
    ADD_ITEM_ENTITY: int = 0x1f
    TAKE_ITEM_ENTITY: int = 0x11
    MOVE_ENTITY: int = 0x12
    MOVE_PLAYER: int = 0x13
    RIDER_JUMP: int = 0x14
    UPDATE_BLOCK: int = 0x15
    ADD_PAINTING: int = 0x16
    TICK_SYNC: int = 0x17
    LEVEL_SOUND_EVENT_OLD: int = 0x18
    LEVEL_EVENT: int = 0x19
    BLOCK_EVENT: int = 0x1a
    ENTITY_EVENT: int = 0x1b
    MOB_EFFECT: int = 0x1c
    UPDATE_ATTRIBUTES: int = 0x1d
    INVENTORY_TRANSACTION: int = 0x1e
    MOB_EQUIPMENT: int = 0x1f
    MOB_ARMOR_EQUIPMENT: int = 0x20
    INTERACT: int = 0x21
    BLOCK_PICK_REQUEST: int = 0x22
    ENTITY_PICK_REQUEST: int = 0x23
    PLAYER_ACTION: int = 0x24
    HURT_ARMOR: int = 0x25
    SET_ENTITY_DATA: int = 0x27
    SET_ENTITY_MOTION: int = 0x28
    SET_ENTITY_LINK: int = 0x29
    SET_HEALTH: int = 0x2a
    SET_SPAWN_POSITION: int = 0x2b
    ANIMATE: int = 0x2c
    RESPAWN: int = 0x2d
    CONTAINER_OPEN: int = 0x2e
    CONTAINER_CLOSE: int = 0x2f
    PLAYER_HOTBAR: int = 0x30
    INVENTORY_CONTENT: int = 0x31
    INVENTORY_SLOT: int = 0x32
    CONTAINER_SET_DATA: int = 0x33
    CRAFTING_DATA: int = 0x34
    CRAFTING_EVENT: int = 0x35
    GUI_DATA_PICK_ITEM: int = 0x36
    ADVENTURE_SETTINGS: int = 0x37
    BLOCK_ENTITY_DATA: int = 0x38
    PLAYER_INPUT: int = 0x39
    LEVEL_CHUNK: int = 0x3a
    SET_COMMANDS_ENABLED: int = 0x3b
    SET_DIFFICULTY: int = 0x3c
    CHANGE_DIMENSION: int = 0x3d
    SET_PLAYER_GAME_TYPE: int = 0x3e
    PLAYER_LIST: int = 0x3f
    SIMPLE_EVENT: int = 0x40
    TELEMETRY_EVENT: int = 0x41
    SPAWN_EXPERIENCE_ORB: int = 0x42
    CLIENTBOUND_MAP_ITEM_DATA: int = 0x43
    MAP_INFO_REQUEST: int = 0x44
    REQUEST_CHUNK_RADIUS: int = 0x45
    CHUNK_RADIUS_UPDATE: int = 0x46
    ITEM_FRAME_DROP_ITEM: int = 0x47
    GAME_RULES_CHANGED: int = 0x48
    CAMERA: int = 0x49
    BOSS_EVENT: int = 0x4a
    SHOW_CREDITS: int = 0x4b
    AVAILABLE_COMMANDS: int = 0x4c
    COMMAND_REQUEST: int = 0x4d
    COMMAND_BLOCK_UPDATE: int = 0x4e
    COMMAND_OUTPUT: int = 0x4f
    UPDATE_TRADE: int = 0x50
    UPDATE_EQUIPMENT: int = 0x51
    RESOURCE_PACK_DATA_INFO: int = 0x52
    RESOURCE_PACK_CHUNK_DATA: int = 0x53
    RESOURCE_PACK_CHUNK_REQUEST: int = 0x54
    TRANSFER: int = 0x55
    PLAY_SOUND: int = 0x56
    STOP_SOUND: int = 0x57
    SET_TITLE: int = 0x58
    ADD_BEHAVIOR_TREE: int = 0x59
    STRUCTURE_BLOCK_UPDATE: int = 0x5a
    SHOW_STORE_OFFER: int = 0x5b
    PURCHASE_RECEIPT: int = 0x5c
    PLAYER_SKIN: int = 0x5d
    SUB_CLIENT_LOGIN: int = 0x5e
    INITIATE_WEBSOCKET_CONNECTION: int = 0x5f
    SET_LAST_HURT_BY: int = 0x60
    BOOK_EDIT: int = 0x61
    NPC_REQUEST: int = 0x62
    PHOTO_TRANSFER: int = 0x63
    MODAL_FORM_REQUEST: int = 0x64
    MODAL_FORM_RESPONSE: int = 0x65
    SERVER_SETTINGS_REQUEST: int = 0x66
    SERVER_SETTINGS_RESPONSE: int = 0x67
    SHOW_PROFILE: int = 0x68
    SET_DEFAULT_GAME_TYPE: int = 0x69
    REMOVE_OBJECTIVE: int = 0x6a
    SET_DISPLAY_OBJECTIVE: int = 0x6b
    SET_SCORE: int = 0x6c
    LAB_TABLE: int = 0x6d
    UPDATE_BLOCK_SYNCED: int = 0x6e
    MOVE_ENTITY_DELTA: int = 0x6f
    SET_SCOREBOARD_IDENTITY: int = 0x70
    SET_LOCAL_PLAYER_AS_INITIALIZED: int = 0x71
    UPDATE_SOFT_ENUM: int = 0x72
    NETWORK_STACK_LATENCY: int = 0x73
    SCRIPT_CUSTOM_EVENT: int = 0x75
    SPAWN_PARTICLE_EFFECT: int = 0x76
    AVAILAIBLE_ENTITY_IDENTIFIERS: int = 0x77
    LEVEL_SOUND_EVENT_V2: int = 0x78
    NETWORK_CHUNK_PUBLISHER_UPDATE: int = 0x79
    BIOME_DEFINITON_LIST: int = 0x7a
    LEVEL_SOUND_EVENT: int = 0x7b
    LEVEL_EVENT_GENERIC: int = 0x7c
    LECTERN_UPDATE: int = 0x7d
    VIDEO_STREAM_CONNECT: int = 0x7e
    CLIENT_CACHE_STATUS: int = 0x81
    ON_SCREEN_TEXTURE_ANIMATION: int = 0x82
    MAP_CREATE_LOCKED_COPY: int = 0x83
    STRUCTURE_TEMPLATE_DATA_EXPORT_REQUEST: int = 0x84
    STRUCTURE_TEMPLATE_DATA_EXPORT_RESPONSE: int = 0x85
    UPDATE_BLOCK_PROPERTIES: int = 0x86
    CLIENT_CACHE_BLOB_STATUS: int = 0x87
    CLIENT_CACHE_MISS_RESPONSE: int = 0x88
    NETWORK_SETTINGS: int = 0x8f
    PLAYER_AUTH_INPUT: int = 0x90
    CREATIVE_CONTENT: int = 0x91
    PLAYER_ENCHANT_OPTIONS: int = 0x92
    ITEM_STACK_REQUEST: int = 0x93
    ITEM_STACK_RESPONSE: int = 0x94
    UPDATE_PLAYER_GAME_TYPE: int = 0x97
    PLAYER_VIOLATION_WARNING: int = 0x9c
    ITEM_COMPONENT: int = 0xa2
    FILTER_TEXT_PACKET: int = 0xa3
    UPDATE_SUB_CHUNK_BLOCKS_PACKET: int = 0xac
    SUB_CHUNK_PACKET: int = 0xae
    SUB_CHUNK_REQUEST_PACKET: int = 0xaf
    DIMENSION_DATA: int = 0xb4
    ALEX_ENTITY_ANIMATION: int = 0xe0