{
  'targets': [
    {
      'target_name': 'miniupnpc',
      'type': 'static_library',
      'include_dirs': [
        '<(DEPTH)/third_party/miniupnpc',
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          '<(DEPTH)/third_party/miniupnpc',
        ],
      },
      'sources': [
        'miniwget.c',
        'minixml.c',
        'igd_desc_parse.c',
        'minisoap.c',
        'miniupnpc.c',
        'upnpreplyparse.c',
        'upnpcommands.c',
        'upnperrors.c',
        'connecthostport.c',
        'portlistingparse.c',
        'receivedata.c',
        'minissdpc.c',
      ],
      'conditions': [
        ['OS == "win"', {
          'defines': [
            'STATICLIB',
          ],
          'direct_dependent_settings': {
            'defines': [
              'STATICLIB',
            ],
            'msvs_settings': {
              'VCLinkerTool': {
                'AdditionalDependencies': [
                  'IpHlpApi.Lib',
                ],
              },
            },
          },
          'sources!': [
            'minissdpc.c',
          ],
        }, {
          'defines': [
            'MINIUPNPC_SET_SOCKET_TIMEOUT',
            'MINIUPNPC_GET_SRC_ADDR',
            '_BSD_SOURCE',
            '_POSIX_C_SOURCE=1',
          ],
        }],
        ['OS == "mac"', {
          'defines': [
            'MACOSX',
            '_DARWIN_C_SOURCE',
          ],
        }],
      ],
    },
    {
      'target_name': 'upnpc-static',
      'type': 'executable',
      'sources': [
        'upnpc.c',
      ],
      'dependencies': [
        'miniupnpc',
      ],
    },
  ],
}
