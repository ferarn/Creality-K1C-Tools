# decompyle3 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.14.4 | packaged by Anaconda, Inc. | (main, Apr 14 2026, 17:00:17) [MSC v.1942 64 bit (AMD64)]
# Embedded file name: /var/jenkins_home/workspace/IngenicX2600-CFS-C-Master-Security-Build/integrated_platform/buildtools/../creality/output/build/klipper-creality/klippy/extras/aht10.py
# Compiled at: 2025-10-29 02:45:24
# Size of source mod 2**32: 5712 bytes
               expr ::= LOAD_CONST (1)
               return_expr ::= expr (1)
         2     expr ::= LOAD_CONST (2)
         6     store ::= STORE_NAME (4)
         4-6   alias ::= IMPORT_NAME store (4)
         4-6   alias37 ::= IMPORT_NAME store (4)
               import ::= LOAD_CONST LOAD_CONST alias (4)
         4     importlist ::= alias (4)
         4     importlist37 ::= alias37 (4)
               stmt ::= import (4)
         4     importlists ::= importlist37 (4)
               stmts ::= stmt (4)
               sstmt ::= stmt (4)
               c_stmt ::= stmt (4)
               START ::= |- stmts (4)
               _stmts ::= stmts (4)
               stmts ::= sstmt (4)
               c_stmts ::= c_stmt (4)
               c_stmts ::= _stmts (4)
L.  7:   8     expr ::= LOAD_CONST (5)
L.  7:   8     expr ::= LOAD_CONST (5)
L.  7:   8     return_expr ::= expr (5)
L.  7:   8     return_expr ::= expr (5)
        10     expr ::= LOAD_CONST (6)
        16     store ::= STORE_NAME (9)
        14-16  alias ::= IMPORT_FROM store (9)
        14     importlist ::= alias (9)
L.  7:   8-18  import_from ::= LOAD_CONST LOAD_CONST IMPORT_NAME importlist POP_TOP (10)
L.  7:   8     stmt ::= import_from (10)
               stmts ::= stmts stmt (10)
L.  7:   8     stmts ::= stmt (10)
L.  7:   8     sstmt ::= stmt (10)
L.  7:   8     c_stmt ::= stmt (10)
               START ::= |- stmts (10)
               _stmts ::= stmts (10)
L.  7:   8     _stmts ::= stmts (10)
               stmts ::= stmts sstmt (10)
L.  7:   8     stmts ::= sstmt (10)
L.  7:   8     c_stmts ::= c_stmt (10)
               c_stmts ::= c_stmts c_stmt (10)
               c_stmts ::= _stmts (10)
L.  7:   8     c_stmts ::= _stmts (10)
L. 16:  20     expr ::= LOAD_CONST (11)
L. 16:  20     expr ::= LOAD_CONST (11)
L. 16:  20     return_expr ::= expr (11)
L. 16:  20     return_expr ::= expr (11)
        22     store ::= STORE_NAME (12)
L. 16:  20-22  assign ::= expr store (12)
L. 16:  20     stmt ::= assign (12)
               stmts ::= stmts stmt (12)
L. 16:  20     stmts ::= stmt (12)
L. 16:  20     sstmt ::= stmt (12)
L. 16:  20     c_stmt ::= stmt (12)
L.  7:   8-22  stmts ::= stmts stmt (12)
               START ::= |- stmts (12)
               _stmts ::= stmts (12)
L. 16:  20     _stmts ::= stmts (12)
               stmts ::= stmts sstmt (12)
L. 16:  20     stmts ::= sstmt (12)
L.  7:   8-22  stmts ::= stmts sstmt (12)
L. 16:  20     c_stmts ::= c_stmt (12)
L.  7:   8-22  c_stmts ::= c_stmts c_stmt (12)
               c_stmts ::= c_stmts c_stmt (12)
L.  7:   8     _stmts ::= stmts (12)
               c_stmts ::= _stmts (12)
L. 16:  20     c_stmts ::= _stmts (12)
L.  7:   8     c_stmts ::= _stmts (12)
L. 19:  24     expr ::= LOAD_CONST (13)
L. 19:  24     expr ::= LOAD_CONST (13)
L. 19:  24     return_expr ::= expr (13)
L. 19:  24     return_expr ::= expr (13)
        26     expr ::= LOAD_CONST (14)
        28     expr ::= LOAD_CONST (15)
L. 19:  24-30  list ::= expr expr expr BUILD_LIST_3 (16)
L. 19:  24     expr ::= list (16)
L. 19:  24     return_expr ::= expr (16)
L. 19:  24     return_expr ::= expr (16)
L. 20:  32     expr ::= LOAD_CONST (17)
        34     expr ::= LOAD_CONST (18)
        36     expr ::= LOAD_CONST (19)
L. 20:  32-38  list ::= expr expr expr BUILD_LIST_3 (20)
L. 20:  32     expr ::= list (20)
L. 21:  40     expr ::= LOAD_CONST (21)
        42     expr ::= LOAD_CONST (22)
        44     expr ::= LOAD_CONST (23)
L. 21:  40-46  list ::= expr expr expr BUILD_LIST_3 (24)
L. 21:  40     expr ::= list (24)
L. 18:  48     expr ::= LOAD_CONST (25)
L. 19:  24-50  dict ::= expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_3 (26)
L. 19:  24     expr ::= dict (26)
L. 19:  24     return_expr ::= expr (26)
L. 19:  24     return_expr ::= expr (26)
        52     store ::= STORE_NAME (27)
L. 19:  24-52  assign ::= expr store (27)
L. 19:  24     stmt ::= assign (27)
               stmts ::= stmts stmt (27)
L. 19:  24     stmts ::= stmt (27)
L. 19:  24     sstmt ::= stmt (27)
L. 19:  24     c_stmt ::= stmt (27)
L. 16:  20-52  stmts ::= stmts stmt (27)
L.  7:   8-52  stmts ::= stmts stmt (27)
               START ::= |- stmts (27)
               _stmts ::= stmts (27)
L. 19:  24     _stmts ::= stmts (27)
               stmts ::= stmts sstmt (27)
L. 19:  24     stmts ::= sstmt (27)
L. 16:  20-52  stmts ::= stmts sstmt (27)
L.  7:   8-52  stmts ::= stmts sstmt (27)
L. 19:  24     c_stmts ::= c_stmt (27)
L. 16:  20-52  c_stmts ::= c_stmts c_stmt (27)
L.  7:   8-52  c_stmts ::= c_stmts c_stmt (27)
               c_stmts ::= c_stmts c_stmt (27)
L. 16:  20     _stmts ::= stmts (27)
L.  7:   8     _stmts ::= stmts (27)
               c_stmts ::= _stmts (27)
L. 19:  24     c_stmts ::= _stmts (27)
L. 16:  20     c_stmts ::= _stmts (27)
L.  7:   8     c_stmts ::= _stmts (27)
L. 24:  54     expr ::= LOAD_CONST (28)
L. 24:  54     expr ::= LOAD_CONST (28)
L. 24:  54     return_expr ::= expr (28)
L. 24:  54     return_expr ::= expr (28)
        56     store ::= STORE_NAME (29)
L. 24:  54-56  assign ::= expr store (29)
L. 24:  54     stmt ::= assign (29)
               stmts ::= stmts stmt (29)
L. 24:  54     stmts ::= stmt (29)
L. 24:  54     sstmt ::= stmt (29)
L. 24:  54     c_stmt ::= stmt (29)
L. 19:  24-56  stmts ::= stmts stmt (29)
L. 16:  20-56  stmts ::= stmts stmt (29)
L.  7:   8-56  stmts ::= stmts stmt (29)
               START ::= |- stmts (29)
               _stmts ::= stmts (29)
L. 24:  54     _stmts ::= stmts (29)
               stmts ::= stmts sstmt (29)
L. 24:  54     stmts ::= sstmt (29)
L. 19:  24-56  stmts ::= stmts sstmt (29)
L. 16:  20-56  stmts ::= stmts sstmt (29)
L.  7:   8-56  stmts ::= stmts sstmt (29)
L. 24:  54     c_stmts ::= c_stmt (29)
L. 19:  24-56  c_stmts ::= c_stmts c_stmt (29)
L. 16:  20-56  c_stmts ::= c_stmts c_stmt (29)
L.  7:   8-56  c_stmts ::= c_stmts c_stmt (29)
               c_stmts ::= c_stmts c_stmt (29)
L. 19:  24     _stmts ::= stmts (29)
L. 16:  20     _stmts ::= stmts (29)
L.  7:   8     _stmts ::= stmts (29)
               c_stmts ::= _stmts (29)
L. 24:  54     c_stmts ::= _stmts (29)
L. 19:  24     c_stmts ::= _stmts (29)
L. 16:  20     c_stmts ::= _stmts (29)
L.  7:   8     c_stmts ::= _stmts (29)
        60-64  mkfunc ::= LOAD_CODE LOAD_STR MAKE_FUNCTION_0 (33)
        66     expr ::= LOAD_STR (34)
L. 26:  58-68  build_class ::= LOAD_BUILD_CLASS mkfunc expr CALL_FUNCTION_2 (35)
        70     store ::= STORE_NAME (36)
L. 26:  58-70  classdef ::= build_class store (36)
L. 26:  58     stmt ::= classdef (36)
               stmts ::= stmts stmt (36)
L. 26:  58     stmts ::= stmt (36)
L. 26:  58     sstmt ::= stmt (36)
L. 26:  58     c_stmt ::= stmt (36)
L. 24:  54-70  stmts ::= stmts stmt (36)
L. 19:  24-70  stmts ::= stmts stmt (36)
L. 16:  20-70  stmts ::= stmts stmt (36)
L.  7:   8-70  stmts ::= stmts stmt (36)
               START ::= |- stmts (36)
               _stmts ::= stmts (36)
L. 26:  58     _stmts ::= stmts (36)
               stmts ::= stmts sstmt (36)
L. 26:  58     stmts ::= sstmt (36)
L. 24:  54-70  stmts ::= stmts sstmt (36)
L. 19:  24-70  stmts ::= stmts sstmt (36)
L. 16:  20-70  stmts ::= stmts sstmt (36)
L.  7:   8-70  stmts ::= stmts sstmt (36)
L. 26:  58     c_stmts ::= c_stmt (36)
L. 24:  54-70  c_stmts ::= c_stmts c_stmt (36)
L. 19:  24-70  c_stmts ::= c_stmts c_stmt (36)
L. 16:  20-70  c_stmts ::= c_stmts c_stmt (36)
L.  7:   8-70  c_stmts ::= c_stmts c_stmt (36)
               c_stmts ::= c_stmts c_stmt (36)
L. 24:  54     _stmts ::= stmts (36)
L. 19:  24     _stmts ::= stmts (36)
L. 16:  20     _stmts ::= stmts (36)
L.  7:   8     _stmts ::= stmts (36)
               c_stmts ::= _stmts (36)
L. 26:  58     c_stmts ::= _stmts (36)
L. 24:  54     c_stmts ::= _stmts (36)
L. 19:  24     c_stmts ::= _stmts (36)
L. 16:  20     c_stmts ::= _stmts (36)
L.  7:   8     c_stmts ::= _stmts (36)
L.159:  72     expr ::= LOAD_CODE (37)
L.159:  72     expr ::= LOAD_CODE (37)
L.159:  72     return_expr ::= expr (37)
L.159:  72     return_expr ::= expr (37)
        74     expr ::= LOAD_STR (38)
L.159:  72-76  mkfunc ::= LOAD_CODE LOAD_STR MAKE_FUNCTION_0 (39)
               store ::= STORE_NAME (40)
               function_def ::= mkfunc store (40)
               stmt ::= function_def (40)
               stmts ::= stmts stmt (40)
               stmts ::= stmt (40)
               sstmt ::= stmt (40)
               c_stmt ::= stmt (40)
               stmts ::= stmts stmt (40)
               stmts ::= stmts stmt (40)
               stmts ::= stmts stmt (40)
               stmts ::= stmts stmt (40)
               stmts ::= stmts stmt (40)
               START ::= |- stmts (40)
               _stmts ::= stmts (40)
               _stmts ::= stmts (40)
               stmts ::= stmts sstmt (40)
               stmts ::= sstmt (40)
               stmts ::= stmts sstmt (40)
               stmts ::= stmts sstmt (40)
               stmts ::= stmts sstmt (40)
               stmts ::= stmts sstmt (40)
               stmts ::= stmts sstmt (40)
               c_stmts ::= c_stmt (40)
               c_stmts ::= c_stmts c_stmt (40)
               c_stmts ::= c_stmts c_stmt (40)
               c_stmts ::= c_stmts c_stmt (40)
               c_stmts ::= c_stmts c_stmt (40)
               c_stmts ::= c_stmts c_stmt (40)
               c_stmts ::= c_stmts c_stmt (40)
               _stmts ::= stmts (40)
               _stmts ::= stmts (40)
               _stmts ::= stmts (40)
               _stmts ::= stmts (40)
               _stmts ::= stmts (40)
               c_stmts ::= _stmts (40)
               c_stmts ::= _stmts (40)
               c_stmts ::= _stmts (40)
               c_stmts ::= _stmts (40)
               c_stmts ::= _stmts (40)
               c_stmts ::= _stmts (40)
               c_stmts ::= _stmts (40)
               expr ::= LOAD_NAME (1)
               return_expr ::= expr (1)
         2     store ::= STORE_NAME (2)
               assign ::= expr store (2)
               stmt ::= assign (2)
               stmts ::= stmt (2)
               sstmt ::= stmt (2)
               c_stmt ::= stmt (2)
               START ::= |- stmts (2)
               _stmts ::= stmts (2)
               stmts ::= sstmt (2)
               c_stmts ::= c_stmt (2)
               c_stmts ::= _stmts (2)
         4     expr ::= LOAD_STR (3)
         4     return_expr ::= expr (3)
         4     return_expr ::= expr (3)
         6     store ::= STORE_NAME (4)
         4-6   assign ::= expr store (4)
         4     stmt ::= assign (4)
               stmts ::= stmts stmt (4)
         4     stmts ::= stmt (4)
         4     sstmt ::= stmt (4)
         4     c_stmt ::= stmt (4)
               START ::= |- stmts (4)
               _stmts ::= stmts (4)
         4     _stmts ::= stmts (4)
               stmts ::= stmts sstmt (4)
         4     stmts ::= sstmt (4)
         4     c_stmts ::= c_stmt (4)
               c_stmts ::= c_stmts c_stmt (4)
               c_stmts ::= _stmts (4)
         4     c_stmts ::= _stmts (4)
L. 27:   8     expr ::= LOAD_CODE (5)
L. 27:   8     expr ::= LOAD_CODE (5)
L. 27:   8     return_expr ::= expr (5)
L. 27:   8     return_expr ::= expr (5)
        10     expr ::= LOAD_STR (6)
L. 27:   8-12  mkfunc ::= LOAD_CODE LOAD_STR MAKE_FUNCTION_0 (7)
        14     store ::= STORE_NAME (8)
L. 27:   8-14  function_def ::= mkfunc store (8)
L. 27:   8     stmt ::= function_def (8)
               stmts ::= stmts stmt (8)
L. 27:   8     stmts ::= stmt (8)
L. 27:   8     sstmt ::= stmt (8)
L. 27:   8     c_stmt ::= stmt (8)
         4-14  stmts ::= stmts stmt (8)
               START ::= |- stmts (8)
               _stmts ::= stmts (8)
L. 27:   8     _stmts ::= stmts (8)
               stmts ::= stmts sstmt (8)
L. 27:   8     stmts ::= sstmt (8)
         4-14  stmts ::= stmts sstmt (8)
L. 27:   8     c_stmts ::= c_stmt (8)
         4-14  c_stmts ::= c_stmts c_stmt (8)
               c_stmts ::= c_stmts c_stmt (8)
         4     _stmts ::= stmts (8)
               c_stmts ::= _stmts (8)
L. 27:   8     c_stmts ::= _stmts (8)
         4     c_stmts ::= _stmts (8)
L. 42:  16     expr ::= LOAD_CODE (9)
L. 42:  16     expr ::= LOAD_CODE (9)
L. 42:  16     return_expr ::= expr (9)
L. 42:  16     return_expr ::= expr (9)
        18     expr ::= LOAD_STR (10)
L. 42:  16-20  mkfunc ::= LOAD_CODE LOAD_STR MAKE_FUNCTION_0 (11)
        22     store ::= STORE_NAME (12)
L. 42:  16-22  function_def ::= mkfunc store (12)
L. 42:  16     stmt ::= function_def (12)
               stmts ::= stmts stmt (12)
L. 42:  16     stmts ::= stmt (12)
L. 42:  16     sstmt ::= stmt (12)
L. 42:  16     c_stmt ::= stmt (12)
L. 27:   8-22  stmts ::= stmts stmt (12)
         4-22  stmts ::= stmts stmt (12)
               START ::= |- stmts (12)
               _stmts ::= stmts (12)
L. 42:  16     _stmts ::= stmts (12)
               stmts ::= stmts sstmt (12)
L. 42:  16     stmts ::= sstmt (12)
L. 27:   8-22  stmts ::= stmts sstmt (12)
         4-22  stmts ::= stmts sstmt (12)
L. 42:  16     c_stmts ::= c_stmt (12)
L. 27:   8-22  c_stmts ::= c_stmts c_stmt (12)
         4-22  c_stmts ::= c_stmts c_stmt (12)
               c_stmts ::= c_stmts c_stmt (12)
L. 27:   8     _stmts ::= stmts (12)
         4     _stmts ::= stmts (12)
               c_stmts ::= _stmts (12)
L. 42:  16     c_stmts ::= _stmts (12)
L. 27:   8     c_stmts ::= _stmts (12)
         4     c_stmts ::= _stmts (12)
L. 46:  24     expr ::= LOAD_CODE (13)
L. 46:  24     expr ::= LOAD_CODE (13)
L. 46:  24     return_expr ::= expr (13)
L. 46:  24     return_expr ::= expr (13)
        26     expr ::= LOAD_STR (14)
L. 46:  24-28  mkfunc ::= LOAD_CODE LOAD_STR MAKE_FUNCTION_0 (15)
        30     store ::= STORE_NAME (16)
L. 46:  24-30  function_def ::= mkfunc store (16)
L. 46:  24     stmt ::= function_def (16)
               stmts ::= stmts stmt (16)
L. 46:  24     stmts ::= stmt (16)
L. 46:  24     sstmt ::= stmt (16)
L. 46:  24     c_stmt ::= stmt (16)
L. 42:  16-30  stmts ::= stmts stmt (16)
L. 27:   8-30  stmts ::= stmts stmt (16)
         4-30  stmts ::= stmts stmt (16)
               START ::= |- stmts (16)
               _stmts ::= stmts (16)
L. 46:  24     _stmts ::= stmts (16)
               stmts ::= stmts sstmt (16)
L. 46:  24     stmts ::= sstmt (16)
L. 42:  16-30  stmts ::= stmts sstmt (16)
L. 27:   8-30  stmts ::= stmts sstmt (16)
         4-30  stmts ::= stmts sstmt (16)
L. 46:  24     c_stmts ::= c_stmt (16)
L. 42:  16-30  c_stmts ::= c_stmts c_stmt (16)
L. 27:   8-30  c_stmts ::= c_stmts c_stmt (16)
         4-30  c_stmts ::= c_stmts c_stmt (16)
               c_stmts ::= c_stmts c_stmt (16)
L. 42:  16     _stmts ::= stmts (16)
L. 27:   8     _stmts ::= stmts (16)
         4     _stmts ::= stmts (16)
               c_stmts ::= _stmts (16)
L. 46:  24     c_stmts ::= _stmts (16)
L. 42:  16     c_stmts ::= _stmts (16)
L. 27:   8     c_stmts ::= _stmts (16)
         4     c_stmts ::= _stmts (16)
L. 50:  32     expr ::= LOAD_CODE (17)
L. 50:  32     expr ::= LOAD_CODE (17)
L. 50:  32     return_expr ::= expr (17)
L. 50:  32     return_expr ::= expr (17)
        34     expr ::= LOAD_STR (18)
L. 50:  32-36  mkfunc ::= LOAD_CODE LOAD_STR MAKE_FUNCTION_0 (19)
        38     store ::= STORE_NAME (20)
L. 50:  32-38  function_def ::= mkfunc store (20)
L. 50:  32     stmt ::= function_def (20)
               stmts ::= stmts stmt (20)
L. 50:  32     stmts ::= stmt (20)
L. 50:  32     sstmt ::= stmt (20)
L. 50:  32     c_stmt ::= stmt (20)
L. 46:  24-38  stmts ::= stmts stmt (20)
L. 42:  16-38  stmts ::= stmts stmt (20)
L. 27:   8-38  stmts ::= stmts stmt (20)
         4-38  stmts ::= stmts stmt (20)
               START ::= |- stmts (20)
               _stmts ::= stmts (20)
L. 50:  32     _stmts ::= stmts (20)
               stmts ::= stmts sstmt (20)
L. 50:  32     stmts ::= sstmt (20)
L. 46:  24-38  stmts ::= stmts sstmt (20)
L. 42:  16-38  stmts ::= stmts sstmt (20)
L. 27:   8-38  stmts ::= stmts sstmt (20)
         4-38  stmts ::= stmts sstmt (20)
L. 50:  32     c_stmts ::= c_stmt (20)
L. 46:  24-38  c_stmts ::= c_stmts c_stmt (20)
L. 42:  16-38  c_stmts ::= c_stmts c_stmt (20)
L. 27:   8-38  c_stmts ::= c_stmts c_stmt (20)
         4-38  c_stmts ::= c_stmts c_stmt (20)
               c_stmts ::= c_stmts c_stmt (20)
L. 46:  24     _stmts ::= stmts (20)
L. 42:  16     _stmts ::= stmts (20)
L. 27:   8     _stmts ::= stmts (20)
         4     _stmts ::= stmts (20)
               c_stmts ::= _stmts (20)
L. 50:  32     c_stmts ::= _stmts (20)
L. 46:  24     c_stmts ::= _stmts (20)
L. 42:  16     c_stmts ::= _stmts (20)
L. 27:   8     c_stmts ::= _stmts (20)
         4     c_stmts ::= _stmts (20)
L. 53:  40     expr ::= LOAD_CODE (21)
L. 53:  40     expr ::= LOAD_CODE (21)
L. 53:  40     return_expr ::= expr (21)
L. 53:  40     return_expr ::= expr (21)
        42     expr ::= LOAD_STR (22)
L. 53:  40-44  mkfunc ::= LOAD_CODE LOAD_STR MAKE_FUNCTION_0 (23)
        46     store ::= STORE_NAME (24)
L. 53:  40-46  function_def ::= mkfunc store (24)
L. 53:  40     stmt ::= function_def (24)
               stmts ::= stmts stmt (24)
L. 53:  40     stmts ::= stmt (24)
L. 53:  40     sstmt ::= stmt (24)
L. 53:  40     c_stmt ::= stmt (24)
L. 50:  32-46  stmts ::= stmts stmt (24)
L. 46:  24-46  stmts ::= stmts stmt (24)
L. 42:  16-46  stmts ::= stmts stmt (24)
L. 27:   8-46  stmts ::= stmts stmt (24)
         4-46  stmts ::= stmts stmt (24)
               START ::= |- stmts (24)
               _stmts ::= stmts (24)
L. 53:  40     _stmts ::= stmts (24)
               stmts ::= stmts sstmt (24)
L. 53:  40     stmts ::= sstmt (24)
L. 50:  32-46  stmts ::= stmts sstmt (24)
L. 46:  24-46  stmts ::= stmts sstmt (24)
L. 42:  16-46  stmts ::= stmts sstmt (24)
L. 27:   8-46  stmts ::= stmts sstmt (24)
         4-46  stmts ::= stmts sstmt (24)
L. 53:  40     c_stmts ::= c_stmt (24)
L. 50:  32-46  c_stmts ::= c_stmts c_stmt (24)
L. 46:  24-46  c_stmts ::= c_stmts c_stmt (24)
L. 42:  16-46  c_stmts ::= c_stmts c_stmt (24)
L. 27:   8-46  c_stmts ::= c_stmts c_stmt (24)
         4-46  c_stmts ::= c_stmts c_stmt (24)
               c_stmts ::= c_stmts c_stmt (24)
L. 50:  32     _stmts ::= stmts (24)
L. 46:  24     _stmts ::= stmts (24)
L. 42:  16     _stmts ::= stmts (24)
L. 27:   8     _stmts ::= stmts (24)
         4     _stmts ::= stmts (24)
               c_stmts ::= _stmts (24)
L. 53:  40     c_stmts ::= _stmts (24)
L. 50:  32     c_stmts ::= _stmts (24)
L. 46:  24     c_stmts ::= _stmts (24)
L. 42:  16     c_stmts ::= _stmts (24)
L. 27:   8     c_stmts ::= _stmts (24)
         4     c_stmts ::= _stmts (24)
L. 56:  48     expr ::= LOAD_CODE (25)
L. 56:  48     expr ::= LOAD_CODE (25)
L. 56:  48     return_expr ::= expr (25)
L. 56:  48     return_expr ::= expr (25)
        50     expr ::= LOAD_STR (26)
L. 56:  48-52  mkfunc ::= LOAD_CODE LOAD_STR MAKE_FUNCTION_0 (27)
        54     store ::= STORE_NAME (28)
L. 56:  48-54  function_def ::= mkfunc store (28)
L. 56:  48     stmt ::= function_def (28)
               stmts ::= stmts stmt (28)
L. 56:  48     stmts ::= stmt (28)
L. 56:  48     sstmt ::= stmt (28)
L. 56:  48     c_stmt ::= stmt (28)
L. 53:  40-54  stmts ::= stmts stmt (28)
L. 50:  32-54  stmts ::= stmts stmt (28)
L. 46:  24-54  stmts ::= stmts stmt (28)
L. 42:  16-54  stmts ::= stmts stmt (28)
L. 27:   8-54  stmts ::= stmts stmt (28)
         4-54  stmts ::= stmts stmt (28)
               START ::= |- stmts (28)
               _stmts ::= stmts (28)
L. 56:  48     _stmts ::= stmts (28)
               stmts ::= stmts sstmt (28)
L. 56:  48     stmts ::= sstmt (28)
L. 53:  40-54  stmts ::= stmts sstmt (28)
L. 50:  32-54  stmts ::= stmts sstmt (28)
L. 46:  24-54  stmts ::= stmts sstmt (28)
L. 42:  16-54  stmts ::= stmts sstmt (28)
L. 27:   8-54  stmts ::= stmts sstmt (28)
         4-54  stmts ::= stmts sstmt (28)
L. 56:  48     c_stmts ::= c_stmt (28)
L. 53:  40-54  c_stmts ::= c_stmts c_stmt (28)
L. 50:  32-54  c_stmts ::= c_stmts c_stmt (28)
L. 46:  24-54  c_stmts ::= c_stmts c_stmt (28)
L. 42:  16-54  c_stmts ::= c_stmts c_stmt (28)
L. 27:   8-54  c_stmts ::= c_stmts c_stmt (28)
         4-54  c_stmts ::= c_stmts c_stmt (28)
               c_stmts ::= c_stmts c_stmt (28)
L. 53:  40     _stmts ::= stmts (28)
L. 50:  32     _stmts ::= stmts (28)
L. 46:  24     _stmts ::= stmts (28)
L. 42:  16     _stmts ::= stmts (28)
L. 27:   8     _stmts ::= stmts (28)
         4     _stmts ::= stmts (28)
               c_stmts ::= _stmts (28)
L. 56:  48     c_stmts ::= _stmts (28)
L. 53:  40     c_stmts ::= _stmts (28)
L. 50:  32     c_stmts ::= _stmts (28)
L. 46:  24     c_stmts ::= _stmts (28)
L. 42:  16     c_stmts ::= _stmts (28)
L. 27:   8     c_stmts ::= _stmts (28)
         4     c_stmts ::= _stmts (28)
L.117:  56     expr ::= LOAD_CODE (29)
L.117:  56     expr ::= LOAD_CODE (29)
L.117:  56     return_expr ::= expr (29)
L.117:  56     return_expr ::= expr (29)
        58     expr ::= LOAD_STR (30)
L.117:  56-60  mkfunc ::= LOAD_CODE LOAD_STR MAKE_FUNCTION_0 (31)
        62     store ::= STORE_NAME (32)
L.117:  56-62  function_def ::= mkfunc store (32)
L.117:  56     stmt ::= function_def (32)
               stmts ::= stmts stmt (32)
L.117:  56     stmts ::= stmt (32)
L.117:  56     sstmt ::= stmt (32)
L.117:  56     c_stmt ::= stmt (32)
L. 56:  48-62  stmts ::= stmts stmt (32)
L. 53:  40-62  stmts ::= stmts stmt (32)
L. 50:  32-62  stmts ::= stmts stmt (32)
L. 46:  24-62  stmts ::= stmts stmt (32)
L. 42:  16-62  stmts ::= stmts stmt (32)
L. 27:   8-62  stmts ::= stmts stmt (32)
         4-62  stmts ::= stmts stmt (32)
               START ::= |- stmts (32)
               _stmts ::= stmts (32)
L.117:  56     _stmts ::= stmts (32)
               stmts ::= stmts sstmt (32)
L.117:  56     stmts ::= sstmt (32)
L. 56:  48-62  stmts ::= stmts sstmt (32)
L. 53:  40-62  stmts ::= stmts sstmt (32)
L. 50:  32-62  stmts ::= stmts sstmt (32)
L. 46:  24-62  stmts ::= stmts sstmt (32)
L. 42:  16-62  stmts ::= stmts sstmt (32)
L. 27:   8-62  stmts ::= stmts sstmt (32)
         4-62  stmts ::= stmts sstmt (32)
L.117:  56     c_stmts ::= c_stmt (32)
L. 56:  48-62  c_stmts ::= c_stmts c_stmt (32)
L. 53:  40-62  c_stmts ::= c_stmts c_stmt (32)
L. 50:  32-62  c_stmts ::= c_stmts c_stmt (32)
L. 46:  24-62  c_stmts ::= c_stmts c_stmt (32)
L. 42:  16-62  c_stmts ::= c_stmts c_stmt (32)
L. 27:   8-62  c_stmts ::= c_stmts c_stmt (32)
         4-62  c_stmts ::= c_stmts c_stmt (32)
               c_stmts ::= c_stmts c_stmt (32)
L. 56:  48     _stmts ::= stmts (32)
L. 53:  40     _stmts ::= stmts (32)
L. 50:  32     _stmts ::= stmts (32)
L. 46:  24     _stmts ::= stmts (32)
L. 42:  16     _stmts ::= stmts (32)
L. 27:   8     _stmts ::= stmts (32)
         4     _stmts ::= stmts (32)
               c_stmts ::= _stmts (32)
L.117:  56     c_stmts ::= _stmts (32)
L. 56:  48     c_stmts ::= _stmts (32)
L. 53:  40     c_stmts ::= _stmts (32)
L. 50:  32     c_stmts ::= _stmts (32)
L. 46:  24     c_stmts ::= _stmts (32)
L. 42:  16     c_stmts ::= _stmts (32)
L. 27:   8     c_stmts ::= _stmts (32)
         4     c_stmts ::= _stmts (32)
L.126:  64     expr ::= LOAD_CODE (33)
L.126:  64     expr ::= LOAD_CODE (33)
L.126:  64     return_expr ::= expr (33)
L.126:  64     return_expr ::= expr (33)
        66     expr ::= LOAD_STR (34)
L.126:  64-68  mkfunc ::= LOAD_CODE LOAD_STR MAKE_FUNCTION_0 (35)
        70     store ::= STORE_NAME (36)
L.126:  64-70  function_def ::= mkfunc store (36)
L.126:  64     stmt ::= function_def (36)
               stmts ::= stmts stmt (36)
L.126:  64     stmts ::= stmt (36)
L.126:  64     sstmt ::= stmt (36)
L.126:  64     c_stmt ::= stmt (36)
L.117:  56-70  stmts ::= stmts stmt (36)
L. 56:  48-70  stmts ::= stmts stmt (36)
L. 53:  40-70  stmts ::= stmts stmt (36)
L. 50:  32-70  stmts ::= stmts stmt (36)
L. 46:  24-70  stmts ::= stmts stmt (36)
L. 42:  16-70  stmts ::= stmts stmt (36)
L. 27:   8-70  stmts ::= stmts stmt (36)
         4-70  stmts ::= stmts stmt (36)
               START ::= |- stmts (36)
               _stmts ::= stmts (36)
L.126:  64     _stmts ::= stmts (36)
               stmts ::= stmts sstmt (36)
L.126:  64     stmts ::= sstmt (36)
L.117:  56-70  stmts ::= stmts sstmt (36)
L. 56:  48-70  stmts ::= stmts sstmt (36)
L. 53:  40-70  stmts ::= stmts sstmt (36)
L. 50:  32-70  stmts ::= stmts sstmt (36)
L. 46:  24-70  stmts ::= stmts sstmt (36)
L. 42:  16-70  stmts ::= stmts sstmt (36)
L. 27:   8-70  stmts ::= stmts sstmt (36)
         4-70  stmts ::= stmts sstmt (36)
L.126:  64     c_stmts ::= c_stmt (36)
L.117:  56-70  c_stmts ::= c_stmts c_stmt (36)
L. 56:  48-70  c_stmts ::= c_stmts c_stmt (36)
L. 53:  40-70  c_stmts ::= c_stmts c_stmt (36)
L. 50:  32-70  c_stmts ::= c_stmts c_stmt (36)
L. 46:  24-70  c_stmts ::= c_stmts c_stmt (36)
L. 42:  16-70  c_stmts ::= c_stmts c_stmt (36)
L. 27:   8-70  c_stmts ::= c_stmts c_stmt (36)
         4-70  c_stmts ::= c_stmts c_stmt (36)
               c_stmts ::= c_stmts c_stmt (36)
L.117:  56     _stmts ::= stmts (36)
L. 56:  48     _stmts ::= stmts (36)
L. 53:  40     _stmts ::= stmts (36)
L. 50:  32     _stmts ::= stmts (36)
L. 46:  24     _stmts ::= stmts (36)
L. 42:  16     _stmts ::= stmts (36)
L. 27:   8     _stmts ::= stmts (36)
         4     _stmts ::= stmts (36)
               c_stmts ::= _stmts (36)
L.126:  64     c_stmts ::= _stmts (36)
L.117:  56     c_stmts ::= _stmts (36)
L. 56:  48     c_stmts ::= _stmts (36)
L. 53:  40     c_stmts ::= _stmts (36)
L. 50:  32     c_stmts ::= _stmts (36)
L. 46:  24     c_stmts ::= _stmts (36)
L. 42:  16     c_stmts ::= _stmts (36)
L. 27:   8     c_stmts ::= _stmts (36)
         4     c_stmts ::= _stmts (36)
L.137:  72     expr ::= LOAD_CODE (37)
L.137:  72     expr ::= LOAD_CODE (37)
L.137:  72     return_expr ::= expr (37)
L.137:  72     return_expr ::= expr (37)
        74     expr ::= LOAD_STR (38)
L.137:  72-76  mkfunc ::= LOAD_CODE LOAD_STR MAKE_FUNCTION_0 (39)
        78     store ::= STORE_NAME (40)
L.137:  72-78  function_def ::= mkfunc store (40)
L.137:  72     stmt ::= function_def (40)
               stmts ::= stmts stmt (40)
L.137:  72     stmts ::= stmt (40)
L.137:  72     sstmt ::= stmt (40)
L.137:  72     c_stmt ::= stmt (40)
L.126:  64-78  stmts ::= stmts stmt (40)
L.117:  56-78  stmts ::= stmts stmt (40)
L. 56:  48-78  stmts ::= stmts stmt (40)
L. 53:  40-78  stmts ::= stmts stmt (40)
L. 50:  32-78  stmts ::= stmts stmt (40)
L. 46:  24-78  stmts ::= stmts stmt (40)
L. 42:  16-78  stmts ::= stmts stmt (40)
L. 27:   8-78  stmts ::= stmts stmt (40)
         4-78  stmts ::= stmts stmt (40)
               START ::= |- stmts (40)
               _stmts ::= stmts (40)
L.137:  72     _stmts ::= stmts (40)
               stmts ::= stmts sstmt (40)
L.137:  72     stmts ::= sstmt (40)
L.126:  64-78  stmts ::= stmts sstmt (40)
L.117:  56-78  stmts ::= stmts sstmt (40)
L. 56:  48-78  stmts ::= stmts sstmt (40)
L. 53:  40-78  stmts ::= stmts sstmt (40)
L. 50:  32-78  stmts ::= stmts sstmt (40)
L. 46:  24-78  stmts ::= stmts sstmt (40)
L. 42:  16-78  stmts ::= stmts sstmt (40)
L. 27:   8-78  stmts ::= stmts sstmt (40)
         4-78  stmts ::= stmts sstmt (40)
L.137:  72     c_stmts ::= c_stmt (40)
L.126:  64-78  c_stmts ::= c_stmts c_stmt (40)
L.117:  56-78  c_stmts ::= c_stmts c_stmt (40)
L. 56:  48-78  c_stmts ::= c_stmts c_stmt (40)
L. 53:  40-78  c_stmts ::= c_stmts c_stmt (40)
L. 50:  32-78  c_stmts ::= c_stmts c_stmt (40)
L. 46:  24-78  c_stmts ::= c_stmts c_stmt (40)
L. 42:  16-78  c_stmts ::= c_stmts c_stmt (40)
L. 27:   8-78  c_stmts ::= c_stmts c_stmt (40)
         4-78  c_stmts ::= c_stmts c_stmt (40)
               c_stmts ::= c_stmts c_stmt (40)
L.126:  64     _stmts ::= stmts (40)
L.117:  56     _stmts ::= stmts (40)
L. 56:  48     _stmts ::= stmts (40)
L. 53:  40     _stmts ::= stmts (40)
L. 50:  32     _stmts ::= stmts (40)
L. 46:  24     _stmts ::= stmts (40)
L. 42:  16     _stmts ::= stmts (40)
L. 27:   8     _stmts ::= stmts (40)
         4     _stmts ::= stmts (40)
               c_stmts ::= _stmts (40)
L.137:  72     c_stmts ::= _stmts (40)
L.126:  64     c_stmts ::= _stmts (40)
L.117:  56     c_stmts ::= _stmts (40)
L. 56:  48     c_stmts ::= _stmts (40)
L. 53:  40     c_stmts ::= _stmts (40)
L. 50:  32     c_stmts ::= _stmts (40)
L. 46:  24     c_stmts ::= _stmts (40)
L. 42:  16     c_stmts ::= _stmts (40)
L. 27:   8     c_stmts ::= _stmts (40)
         4     c_stmts ::= _stmts (40)
L.152:  80     expr ::= LOAD_CODE (41)
L.152:  80     expr ::= LOAD_CODE (41)
L.152:  80     return_expr ::= expr (41)
L.152:  80     return_expr ::= expr (41)
        82     expr ::= LOAD_STR (42)
L.152:  80-84  mkfunc ::= LOAD_CODE LOAD_STR MAKE_FUNCTION_0 (43)
               store ::= STORE_NAME (44)
               function_def ::= mkfunc store (44)
               stmt ::= function_def (44)
               stmts ::= stmts stmt (44)
               stmts ::= stmt (44)
               sstmt ::= stmt (44)
               c_stmt ::= stmt (44)
               stmts ::= stmts stmt (44)
               stmts ::= stmts stmt (44)
               stmts ::= stmts stmt (44)
               stmts ::= stmts stmt (44)
               stmts ::= stmts stmt (44)
               stmts ::= stmts stmt (44)
               stmts ::= stmts stmt (44)
               stmts ::= stmts stmt (44)
               stmts ::= stmts stmt (44)
               stmts ::= stmts stmt (44)
               START ::= |- stmts (44)
               _stmts ::= stmts (44)
               _stmts ::= stmts (44)
               stmts ::= stmts sstmt (44)
               stmts ::= sstmt (44)
               stmts ::= stmts sstmt (44)
               stmts ::= stmts sstmt (44)
               stmts ::= stmts sstmt (44)
               stmts ::= stmts sstmt (44)
               stmts ::= stmts sstmt (44)
               stmts ::= stmts sstmt (44)
               stmts ::= stmts sstmt (44)
               stmts ::= stmts sstmt (44)
               stmts ::= stmts sstmt (44)
               stmts ::= stmts sstmt (44)
               c_stmts ::= c_stmt (44)
               c_stmts ::= c_stmts c_stmt (44)
               c_stmts ::= c_stmts c_stmt (44)
               c_stmts ::= c_stmts c_stmt (44)
               c_stmts ::= c_stmts c_stmt (44)
               c_stmts ::= c_stmts c_stmt (44)
               c_stmts ::= c_stmts c_stmt (44)
               c_stmts ::= c_stmts c_stmt (44)
               c_stmts ::= c_stmts c_stmt (44)
               c_stmts ::= c_stmts c_stmt (44)
               c_stmts ::= c_stmts c_stmt (44)
               c_stmts ::= c_stmts c_stmt (44)
               _stmts ::= stmts (44)
               _stmts ::= stmts (44)
               _stmts ::= stmts (44)
               _stmts ::= stmts (44)
               _stmts ::= stmts (44)
               _stmts ::= stmts (44)
               _stmts ::= stmts (44)
               _stmts ::= stmts (44)
               _stmts ::= stmts (44)
               _stmts ::= stmts (44)
               c_stmts ::= _stmts (44)
               c_stmts ::= _stmts (44)
               c_stmts ::= _stmts (44)
               c_stmts ::= _stmts (44)
               c_stmts ::= _stmts (44)
               c_stmts ::= _stmts (44)
               c_stmts ::= _stmts (44)
               c_stmts ::= _stmts (44)
               c_stmts ::= _stmts (44)
               c_stmts ::= _stmts (44)
               c_stmts ::= _stmts (44)
               c_stmts ::= _stmts (44)
               expr ::= LOAD_FAST (1)
               return_expr ::= expr (1)
               attribute37 ::= expr LOAD_METHOD (2)
               expr ::= attribute37 (2)
               return_expr ::= expr (2)
               call ::= expr CALL_METHOD_0 (3)
               expr ::= call (3)
               return_expr ::= expr (3)
         6     expr ::= LOAD_FAST (4)
         6-8   store ::= expr STORE_ATTR (5)
               assign ::= expr store (5)
               stmt ::= assign (5)
               stmts ::= stmt (5)
               sstmt ::= stmt (5)
               c_stmt ::= stmt (5)
               START ::= |- stmts (5)
               _stmts ::= stmts (5)
               stmts ::= sstmt (5)
               c_stmts ::= c_stmt (5)
               c_stmts ::= _stmts (5)
L. 29:  10     expr ::= LOAD_FAST (6)
L. 29:  10     return_expr ::= expr (6)
L. 29:  10     return_expr ::= expr (6)
L. 29:  10-12  attribute37 ::= expr LOAD_METHOD (7)
L. 29:  10     expr ::= attribute37 (7)
L. 29:  10     return_expr ::= expr (7)
L. 29:  10     return_expr ::= expr (7)
L. 29:  10-14  call ::= expr CALL_METHOD_0 (8)
L. 29:  10     expr ::= call (8)
L. 29:  10     return_expr ::= expr (8)
L. 29:  10     return_expr ::= expr (8)
L. 29:  10-16  attribute37 ::= expr LOAD_METHOD (9)
L. 29:  10     expr ::= attribute37 (9)
L. 29:  10     return_expr ::= expr (9)
L. 29:  10     return_expr ::= expr (9)
L. 29:  10-18  call ::= expr CALL_METHOD_0 (10)
L. 29:  10     expr ::= call (10)
L. 29:  10     return_expr ::= expr (10)
L. 29:  10     return_expr ::= expr (10)
        20     expr ::= LOAD_CONST (11)
L. 29:  10-22  subscript ::= expr expr BINARY_SUBSCR (12)
L. 29:  10     expr ::= subscript (12)
L. 29:  10     return_expr ::= expr (12)
L. 29:  10     return_expr ::= expr (12)
        24     expr ::= LOAD_FAST (13)
        24-26  store ::= expr STORE_ATTR (14)
L. 29:  10-26  assign ::= expr store (14)
L. 29:  10     stmt ::= assign (14)
               stmts ::= stmts stmt (14)
L. 29:  10     stmts ::= stmt (14)
L. 29:  10     sstmt ::= stmt (14)
L. 29:  10     c_stmt ::= stmt (14)
               START ::= |- stmts (14)
               _stmts ::= stmts (14)
L. 29:  10     _stmts ::= stmts (14)
               stmts ::= stmts sstmt (14)
L. 29:  10     stmts ::= sstmt (14)
L. 29:  10     c_stmts ::= c_stmt (14)
               c_stmts ::= c_stmts c_stmt (14)
               c_stmts ::= _stmts (14)
L. 29:  10     c_stmts ::= _stmts (14)
L. 30:  28     expr ::= LOAD_FAST (15)
L. 30:  28     return_expr ::= expr (15)
L. 30:  28     return_expr ::= expr (15)
L. 30:  28-30  attribute ::= expr LOAD_ATTR (16)
L. 30:  28     expr ::= attribute (16)
L. 30:  28     return_expr ::= expr (16)
L. 30:  28     return_expr ::= expr (16)
L. 30:  28-32  attribute37 ::= expr LOAD_METHOD (17)
L. 30:  28     expr ::= attribute37 (17)
L. 30:  28     return_expr ::= expr (17)
L. 30:  28     return_expr ::= expr (17)
L. 30:  28-34  call ::= expr CALL_METHOD_0 (18)
L. 30:  28     expr ::= call (18)
L. 30:  28     return_expr ::= expr (18)
L. 30:  28     return_expr ::= expr (18)
        36     expr ::= LOAD_FAST (19)
        36-38  store ::= expr STORE_ATTR (20)
L. 30:  28-38  assign ::= expr store (20)
L. 30:  28     stmt ::= assign (20)
               stmts ::= stmts stmt (20)
L. 30:  28     stmts ::= stmt (20)
L. 30:  28     sstmt ::= stmt (20)
L. 30:  28     c_stmt ::= stmt (20)
L. 29:  10-38  stmts ::= stmts stmt (20)
               START ::= |- stmts (20)
               _stmts ::= stmts (20)
L. 30:  28     _stmts ::= stmts (20)
               stmts ::= stmts sstmt (20)
L. 30:  28     stmts ::= sstmt (20)
L. 29:  10-38  stmts ::= stmts sstmt (20)
L. 30:  28     c_stmts ::= c_stmt (20)
L. 29:  10-38  c_stmts ::= c_stmts c_stmt (20)
               c_stmts ::= c_stmts c_stmt (20)
L. 29:  10     _stmts ::= stmts (20)
               c_stmts ::= _stmts (20)
L. 30:  28     c_stmts ::= _stmts (20)
L. 29:  10     c_stmts ::= _stmts (20)
L. 31:  40     expr ::= LOAD_GLOBAL (21)
L. 31:  40     return_expr ::= expr (21)
L. 31:  40     return_expr ::= expr (21)
L. 31:  40-42  attribute ::= expr LOAD_ATTR (22)
L. 31:  40     expr ::= attribute (22)
L. 31:  40     return_expr ::= expr (22)
L. 31:  40     return_expr ::= expr (22)
L. 32:  44     expr ::= LOAD_FAST (23)
L. 32:  46     expr ::= LOAD_GLOBAL (24)
L. 32:  48     expr ::= LOAD_CONST (25)
L. 31:  50     expr ::= LOAD_CONST (26)
L. 31:  40-52  call_kw36 ::= expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_3 (27)
L. 31:  40     expr ::= call_kw36 (27)
L. 31:  40     return_expr ::= expr (27)
L. 31:  40     return_expr ::= expr (27)
        54     expr ::= LOAD_FAST (28)
        54-56  store ::= expr STORE_ATTR (29)
L. 31:  40-56  assign ::= expr store (29)
L. 31:  40     stmt ::= assign (29)
               stmts ::= stmts stmt (29)
L. 31:  40     stmts ::= stmt (29)
L. 31:  40     sstmt ::= stmt (29)
L. 31:  40     c_stmt ::= stmt (29)
L. 30:  28-56  stmts ::= stmts stmt (29)
L. 29:  10-56  stmts ::= stmts stmt (29)
               START ::= |- stmts (29)
               _stmts ::= stmts (29)
L. 31:  40     _stmts ::= stmts (29)
               stmts ::= stmts sstmt (29)
L. 31:  40     stmts ::= sstmt (29)
L. 30:  28-56  stmts ::= stmts sstmt (29)
L. 29:  10-56  stmts ::= stmts sstmt (29)
L. 31:  40     c_stmts ::= c_stmt (29)
L. 30:  28-56  c_stmts ::= c_stmts c_stmt (29)
L. 29:  10-56  c_stmts ::= c_stmts c_stmt (29)
               c_stmts ::= c_stmts c_stmt (29)
L. 30:  28     _stmts ::= stmts (29)
L. 29:  10     _stmts ::= stmts (29)
               c_stmts ::= _stmts (29)
L. 31:  40     c_stmts ::= _stmts (29)
L. 30:  28     c_stmts ::= _stmts (29)
L. 29:  10     c_stmts ::= _stmts (29)
L. 33:  58     expr ::= LOAD_FAST (30)
L. 33:  58     return_expr ::= expr (30)
L. 33:  58     return_expr ::= expr (30)
L. 33:  58-60  attribute ::= expr LOAD_ATTR (31)
L. 33:  58     expr ::= attribute (31)
L. 33:  58     return_expr ::= expr (31)
L. 33:  58     return_expr ::= expr (31)
        62     expr ::= LOAD_STR (32)
        64     expr ::= LOAD_CONST (33)
        66     expr ::= LOAD_CONST (34)
        68     expr ::= LOAD_CONST (35)
L. 33:  58-70  call_kw36 ::= expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_3 (36)
L. 33:  58     expr ::= call_kw36 (36)
L. 33:  58     return_expr ::= expr (36)
L. 33:  58     return_expr ::= expr (36)
        72     expr ::= LOAD_FAST (37)
        72-74  store ::= expr STORE_ATTR (38)
L. 33:  58-74  assign ::= expr store (38)
L. 33:  58     stmt ::= assign (38)
               stmts ::= stmts stmt (38)
L. 33:  58     stmts ::= stmt (38)
L. 33:  58     sstmt ::= stmt (38)
L. 33:  58     c_stmt ::= stmt (38)
L. 31:  40-74  stmts ::= stmts stmt (38)
L. 30:  28-74  stmts ::= stmts stmt (38)
L. 29:  10-74  stmts ::= stmts stmt (38)
               START ::= |- stmts (38)
               _stmts ::= stmts (38)
L. 33:  58     _stmts ::= stmts (38)
               stmts ::= stmts sstmt (38)
L. 33:  58     stmts ::= sstmt (38)
L. 31:  40-74  stmts ::= stmts sstmt (38)
L. 30:  28-74  stmts ::= stmts sstmt (38)
L. 29:  10-74  stmts ::= stmts sstmt (38)
L. 33:  58     c_stmts ::= c_stmt (38)
L. 31:  40-74  c_stmts ::= c_stmts c_stmt (38)
L. 30:  28-74  c_stmts ::= c_stmts c_stmt (38)
L. 29:  10-74  c_stmts ::= c_stmts c_stmt (38)
               c_stmts ::= c_stmts c_stmt (38)
L. 31:  40     _stmts ::= stmts (38)
L. 30:  28     _stmts ::= stmts (38)
L. 29:  10     _stmts ::= stmts (38)
               c_stmts ::= _stmts (38)
L. 33:  58     c_stmts ::= _stmts (38)
L. 31:  40     c_stmts ::= _stmts (38)
L. 30:  28     c_stmts ::= _stmts (38)
L. 29:  10     c_stmts ::= _stmts (38)
L. 34:  76     expr ::= LOAD_CONST (39)
L. 34:  76     expr ::= LOAD_CONST (39)
L. 34:  76     return_expr ::= expr (39)
L. 34:  76     return_expr ::= expr (39)
        80     expr ::= LOAD_FAST (41)
        80-82  store ::= expr STORE_ATTR (42)
L. 34:  76-82  named_expr ::= expr DUP_TOP store (42)
L. 34:  76     expr ::= named_expr (42)
L. 34:  76     return_expr ::= expr (42)
L. 34:  76     return_expr ::= expr (42)
        86     expr ::= LOAD_FAST (44)
        86-88  store ::= expr STORE_ATTR (45)
L. 34:  76-88  named_expr ::= expr DUP_TOP store (45)
L. 34:  76     expr ::= named_expr (45)
L. 34:  76     return_expr ::= expr (45)
L. 34:  76     return_expr ::= expr (45)
        92     expr ::= LOAD_FAST (47)
        92-94  store ::= expr STORE_ATTR (48)
L. 34:  76-94  named_expr ::= expr DUP_TOP store (48)
L. 34:  76     expr ::= named_expr (48)
L. 34:  76     return_expr ::= expr (48)
L. 34:  76     return_expr ::= expr (48)
        96     expr ::= LOAD_FAST (49)
        96-98  store ::= expr STORE_ATTR (50)
        92-98  designList ::= store store (50)
L. 34:  76-98  assign ::= expr store (50)
        86-98  designList ::= store DUP_TOP designList (50)
L. 34:  76-98  assign ::= expr DUP_TOP designList (50)
L. 34:  76     stmt ::= assign (50)
        80-98  designList ::= store DUP_TOP designList (50)
               stmts ::= stmts stmt (50)
L. 34:  76     stmts ::= stmt (50)
L. 34:  76     sstmt ::= stmt (50)
L. 34:  76     c_stmt ::= stmt (50)
L. 33:  58-98  stmts ::= stmts stmt (50)
L. 31:  40-98  stmts ::= stmts stmt (50)
L. 30:  28-98  stmts ::= stmts stmt (50)
L. 29:  10-98  stmts ::= stmts stmt (50)
               START ::= |- stmts (50)
               _stmts ::= stmts (50)
L. 34:  76     _stmts ::= stmts (50)
               stmts ::= stmts sstmt (50)
L. 34:  76     stmts ::= sstmt (50)
L. 33:  58-98  stmts ::= stmts sstmt (50)
L. 31:  40-98  stmts ::= stmts sstmt (50)
L. 30:  28-98  stmts ::= stmts sstmt (50)
L. 29:  10-98  stmts ::= stmts sstmt (50)
L. 34:  76     c_stmts ::= c_stmt (50)
L. 33:  58-98  c_stmts ::= c_stmts c_stmt (50)
L. 31:  40-98  c_stmts ::= c_stmts c_stmt (50)
L. 30:  28-98  c_stmts ::= c_stmts c_stmt (50)
L. 29:  10-98  c_stmts ::= c_stmts c_stmt (50)
               c_stmts ::= c_stmts c_stmt (50)
L. 33:  58     _stmts ::= stmts (50)
L. 31:  40     _stmts ::= stmts (50)
L. 30:  28     _stmts ::= stmts (50)
L. 29:  10     _stmts ::= stmts (50)
               c_stmts ::= _stmts (50)
L. 34:  76     c_stmts ::= _stmts (50)
L. 33:  58     c_stmts ::= _stmts (50)
L. 31:  40     c_stmts ::= _stmts (50)
L. 30:  28     c_stmts ::= _stmts (50)
L. 29:  10     c_stmts ::= _stmts (50)
L. 35: 100     expr ::= LOAD_FAST (51)
L. 35: 100     return_expr ::= expr (51)
L. 35: 100     return_expr ::= expr (51)
L. 35: 100-102 attribute ::= expr LOAD_ATTR (52)
L. 35: 100     expr ::= attribute (52)
L. 35: 100     return_expr ::= expr (52)
L. 35: 100     return_expr ::= expr (52)
L. 35: 100-104 attribute37 ::= expr LOAD_METHOD (53)
L. 35: 100     expr ::= attribute37 (53)
L. 35: 100     return_expr ::= expr (53)
L. 35: 100     return_expr ::= expr (53)
       106     expr ::= LOAD_FAST (54)
       106-108 attribute ::= expr LOAD_ATTR (55)
       106     expr ::= attribute (55)
L. 35: 100-110 call ::= expr expr CALL_METHOD_1 (56)
L. 35: 100     expr ::= call (56)
L. 35: 100     return_expr ::= expr (56)
L. 35: 100     return_expr ::= expr (56)
       112     expr ::= LOAD_FAST (57)
       112-114 store ::= expr STORE_ATTR (58)
L. 35: 100-114 assign ::= expr store (58)
L. 35: 100     stmt ::= assign (58)
               stmts ::= stmts stmt (58)
L. 35: 100     stmts ::= stmt (58)
L. 35: 100     sstmt ::= stmt (58)
L. 35: 100     c_stmt ::= stmt (58)
L. 34:  76-114 stmts ::= stmts stmt (58)
L. 33:  58-114 stmts ::= stmts stmt (58)
L. 31:  40-114 stmts ::= stmts stmt (58)
L. 30:  28-114 stmts ::= stmts stmt (58)
L. 29:  10-114 stmts ::= stmts stmt (58)
               START ::= |- stmts (58)
               _stmts ::= stmts (58)
L. 35: 100     _stmts ::= stmts (58)
               stmts ::= stmts sstmt (58)
L. 35: 100     stmts ::= sstmt (58)
L. 34:  76-114 stmts ::= stmts sstmt (58)
L. 33:  58-114 stmts ::= stmts sstmt (58)
L. 31:  40-114 stmts ::= stmts sstmt (58)
L. 30:  28-114 stmts ::= stmts sstmt (58)
L. 29:  10-114 stmts ::= stmts sstmt (58)
L. 35: 100     c_stmts ::= c_stmt (58)
L. 34:  76-114 c_stmts ::= c_stmts c_stmt (58)
L. 33:  58-114 c_stmts ::= c_stmts c_stmt (58)
L. 31:  40-114 c_stmts ::= c_stmts c_stmt (58)
L. 30:  28-114 c_stmts ::= c_stmts c_stmt (58)
L. 29:  10-114 c_stmts ::= c_stmts c_stmt (58)
               c_stmts ::= c_stmts c_stmt (58)
L. 34:  76     _stmts ::= stmts (58)
L. 33:  58     _stmts ::= stmts (58)
L. 31:  40     _stmts ::= stmts (58)
L. 30:  28     _stmts ::= stmts (58)
L. 29:  10     _stmts ::= stmts (58)
               c_stmts ::= _stmts (58)
L. 35: 100     c_stmts ::= _stmts (58)
L. 34:  76     c_stmts ::= _stmts (58)
L. 33:  58     c_stmts ::= _stmts (58)
L. 31:  40     c_stmts ::= _stmts (58)
L. 30:  28     c_stmts ::= _stmts (58)
L. 29:  10     c_stmts ::= _stmts (58)
L. 36: 116     expr ::= LOAD_FAST (59)
L. 36: 116     return_expr ::= expr (59)
L. 36: 116     return_expr ::= expr (59)
L. 36: 116-118 attribute ::= expr LOAD_ATTR (60)
L. 36: 116     expr ::= attribute (60)
L. 36: 116     return_expr ::= expr (60)
L. 36: 116     return_expr ::= expr (60)
L. 36: 116-120 attribute37 ::= expr LOAD_METHOD (61)
L. 36: 116     expr ::= attribute37 (61)
L. 36: 116     return_expr ::= expr (61)
L. 36: 116     return_expr ::= expr (61)
       122     expr ::= LOAD_STR (62)
       124     expr ::= LOAD_FAST (63)
       124-126 attribute ::= expr LOAD_ATTR (64)
       124     expr ::= attribute (64)
       128     binary_operator ::= BINARY_ADD (65)
       122-128 bin_op ::= expr expr binary_operator (65)
       122     expr ::= bin_op (65)
       130     expr ::= LOAD_FAST (66)
L. 36: 116-132 call ::= expr expr expr CALL_METHOD_2 (67)
L. 36: 116     expr ::= call (67)
L. 36: 116     return_expr ::= expr (67)
L. 36: 116     return_expr ::= expr (67)
L. 36: 116-134 expr_stmt ::= expr POP_TOP (68)
L. 36: 116     stmt ::= expr_stmt (68)
               stmts ::= stmts stmt (68)
L. 36: 116     stmts ::= stmt (68)
L. 36: 116     sstmt ::= stmt (68)
L. 36: 116     c_stmt ::= stmt (68)
L. 35: 100-134 stmts ::= stmts stmt (68)
L. 34:  76-134 stmts ::= stmts stmt (68)
L. 33:  58-134 stmts ::= stmts stmt (68)
L. 31:  40-134 stmts ::= stmts stmt (68)
L. 30:  28-134 stmts ::= stmts stmt (68)
L. 29:  10-134 stmts ::= stmts stmt (68)
               START ::= |- stmts (68)
               _stmts ::= stmts (68)
L. 36: 116     _stmts ::= stmts (68)
               stmts ::= stmts sstmt (68)
L. 36: 116     stmts ::= sstmt (68)
L. 35: 100-134 stmts ::= stmts sstmt (68)
L. 34:  76-134 stmts ::= stmts sstmt (68)
L. 33:  58-134 stmts ::= stmts sstmt (68)
L. 31:  40-134 stmts ::= stmts sstmt (68)
L. 30:  28-134 stmts ::= stmts sstmt (68)
L. 29:  10-134 stmts ::= stmts sstmt (68)
L. 36: 116     c_stmts ::= c_stmt (68)
L. 35: 100-134 c_stmts ::= c_stmts c_stmt (68)
L. 34:  76-134 c_stmts ::= c_stmts c_stmt (68)
L. 33:  58-134 c_stmts ::= c_stmts c_stmt (68)
L. 31:  40-134 c_stmts ::= c_stmts c_stmt (68)
L. 30:  28-134 c_stmts ::= c_stmts c_stmt (68)
L. 29:  10-134 c_stmts ::= c_stmts c_stmt (68)
               c_stmts ::= c_stmts c_stmt (68)
L. 35: 100     _stmts ::= stmts (68)
L. 34:  76     _stmts ::= stmts (68)
L. 33:  58     _stmts ::= stmts (68)
L. 31:  40     _stmts ::= stmts (68)
L. 30:  28     _stmts ::= stmts (68)
L. 29:  10     _stmts ::= stmts (68)
               c_stmts ::= _stmts (68)
L. 36: 116     c_stmts ::= _stmts (68)
L. 35: 100     c_stmts ::= _stmts (68)
L. 34:  76     c_stmts ::= _stmts (68)
L. 33:  58     c_stmts ::= _stmts (68)
L. 31:  40     c_stmts ::= _stmts (68)
L. 30:  28     c_stmts ::= _stmts (68)
L. 29:  10     c_stmts ::= _stmts (68)
L. 37: 136     expr ::= LOAD_FAST (69)
L. 37: 136     return_expr ::= expr (69)
L. 37: 136     return_expr ::= expr (69)
L. 37: 136-138 attribute ::= expr LOAD_ATTR (70)
L. 37: 136     expr ::= attribute (70)
L. 37: 136     return_expr ::= expr (70)
L. 37: 136     return_expr ::= expr (70)
L. 37: 136-140 attribute37 ::= expr LOAD_METHOD (71)
L. 37: 136     expr ::= attribute37 (71)
L. 37: 136     return_expr ::= expr (71)
L. 37: 136     return_expr ::= expr (71)
       142     expr ::= LOAD_STR (72)
L. 38: 144     expr ::= LOAD_FAST (73)
L. 38: 144-146 attribute ::= expr LOAD_ATTR (74)
L. 38: 144     expr ::= attribute (74)
L. 37: 136-148 call ::= expr expr expr CALL_METHOD_2 (75)
L. 37: 136     expr ::= call (75)
L. 37: 136     return_expr ::= expr (75)
L. 37: 136     return_expr ::= expr (75)
L. 37: 136-150 expr_stmt ::= expr POP_TOP (76)
L. 37: 136     stmt ::= expr_stmt (76)
               stmts ::= stmts stmt (76)
L. 37: 136     stmts ::= stmt (76)
L. 37: 136     sstmt ::= stmt (76)
L. 37: 136     c_stmt ::= stmt (76)
L. 36: 116-150 stmts ::= stmts stmt (76)
L. 35: 100-150 stmts ::= stmts stmt (76)
L. 34:  76-150 stmts ::= stmts stmt (76)
L. 33:  58-150 stmts ::= stmts stmt (76)
L. 31:  40-150 stmts ::= stmts stmt (76)
L. 30:  28-150 stmts ::= stmts stmt (76)
L. 29:  10-150 stmts ::= stmts stmt (76)
               START ::= |- stmts (76)
               _stmts ::= stmts (76)
L. 37: 136     _stmts ::= stmts (76)
               stmts ::= stmts sstmt (76)
L. 37: 136     stmts ::= sstmt (76)
L. 36: 116-150 stmts ::= stmts sstmt (76)
L. 35: 100-150 stmts ::= stmts sstmt (76)
L. 34:  76-150 stmts ::= stmts sstmt (76)
L. 33:  58-150 stmts ::= stmts sstmt (76)
L. 31:  40-150 stmts ::= stmts sstmt (76)
L. 30:  28-150 stmts ::= stmts sstmt (76)
L. 29:  10-150 stmts ::= stmts sstmt (76)
L. 37: 136     c_stmts ::= c_stmt (76)
L. 36: 116-150 c_stmts ::= c_stmts c_stmt (76)
L. 35: 100-150 c_stmts ::= c_stmts c_stmt (76)
L. 34:  76-150 c_stmts ::= c_stmts c_stmt (76)
L. 33:  58-150 c_stmts ::= c_stmts c_stmt (76)
L. 31:  40-150 c_stmts ::= c_stmts c_stmt (76)
L. 30:  28-150 c_stmts ::= c_stmts c_stmt (76)
L. 29:  10-150 c_stmts ::= c_stmts c_stmt (76)
               c_stmts ::= c_stmts c_stmt (76)
L. 36: 116     _stmts ::= stmts (76)
L. 35: 100     _stmts ::= stmts (76)
L. 34:  76     _stmts ::= stmts (76)
L. 33:  58     _stmts ::= stmts (76)
L. 31:  40     _stmts ::= stmts (76)
L. 30:  28     _stmts ::= stmts (76)
L. 29:  10     _stmts ::= stmts (76)
               c_stmts ::= _stmts (76)
L. 37: 136     c_stmts ::= _stmts (76)
L. 36: 116     c_stmts ::= _stmts (76)
L. 35: 100     c_stmts ::= _stmts (76)
L. 34:  76     c_stmts ::= _stmts (76)
L. 33:  58     c_stmts ::= _stmts (76)
L. 31:  40     c_stmts ::= _stmts (76)
L. 30:  28     c_stmts ::= _stmts (76)
L. 29:  10     c_stmts ::= _stmts (76)
L. 39: 152     expr ::= LOAD_CONST (77)
L. 39: 152     expr ::= LOAD_CONST (77)
L. 39: 152     return_expr ::= expr (77)
L. 39: 152     return_expr ::= expr (77)
       154     expr ::= LOAD_FAST (78)
       154-156 store ::= expr STORE_ATTR (79)
L. 39: 152-156 assign ::= expr store (79)
L. 39: 152     stmt ::= assign (79)
               stmts ::= stmts stmt (79)
L. 39: 152     stmts ::= stmt (79)
L. 39: 152     sstmt ::= stmt (79)
L. 39: 152     c_stmt ::= stmt (79)
L. 37: 136-156 stmts ::= stmts stmt (79)
L. 36: 116-156 stmts ::= stmts stmt (79)
L. 35: 100-156 stmts ::= stmts stmt (79)
L. 34:  76-156 stmts ::= stmts stmt (79)
L. 33:  58-156 stmts ::= stmts stmt (79)
L. 31:  40-156 stmts ::= stmts stmt (79)
L. 30:  28-156 stmts ::= stmts stmt (79)
L. 29:  10-156 stmts ::= stmts stmt (79)
               START ::= |- stmts (79)
               _stmts ::= stmts (79)
L. 39: 152     _stmts ::= stmts (79)
               stmts ::= stmts sstmt (79)
L. 39: 152     stmts ::= sstmt (79)
L. 37: 136-156 stmts ::= stmts sstmt (79)
L. 36: 116-156 stmts ::= stmts sstmt (79)
L. 35: 100-156 stmts ::= stmts sstmt (79)
L. 34:  76-156 stmts ::= stmts sstmt (79)
L. 33:  58-156 stmts ::= stmts sstmt (79)
L. 31:  40-156 stmts ::= stmts sstmt (79)
L. 30:  28-156 stmts ::= stmts sstmt (79)
L. 29:  10-156 stmts ::= stmts sstmt (79)
L. 39: 152     c_stmts ::= c_stmt (79)
L. 37: 136-156 c_stmts ::= c_stmts c_stmt (79)
L. 36: 116-156 c_stmts ::= c_stmts c_stmt (79)
L. 35: 100-156 c_stmts ::= c_stmts c_stmt (79)
L. 34:  76-156 c_stmts ::= c_stmts c_stmt (79)
L. 33:  58-156 c_stmts ::= c_stmts c_stmt (79)
L. 31:  40-156 c_stmts ::= c_stmts c_stmt (79)
L. 30:  28-156 c_stmts ::= c_stmts c_stmt (79)
L. 29:  10-156 c_stmts ::= c_stmts c_stmt (79)
               c_stmts ::= c_stmts c_stmt (79)
L. 37: 136     _stmts ::= stmts (79)
L. 36: 116     _stmts ::= stmts (79)
L. 35: 100     _stmts ::= stmts (79)
L. 34:  76     _stmts ::= stmts (79)
L. 33:  58     _stmts ::= stmts (79)
L. 31:  40     _stmts ::= stmts (79)
L. 30:  28     _stmts ::= stmts (79)
L. 29:  10     _stmts ::= stmts (79)
               c_stmts ::= _stmts (79)
L. 39: 152     c_stmts ::= _stmts (79)
L. 37: 136     c_stmts ::= _stmts (79)
L. 36: 116     c_stmts ::= _stmts (79)
L. 35: 100     c_stmts ::= _stmts (79)
L. 34:  76     c_stmts ::= _stmts (79)
L. 33:  58     c_stmts ::= _stmts (79)
L. 31:  40     c_stmts ::= _stmts (79)
L. 30:  28     c_stmts ::= _stmts (79)
L. 29:  10     c_stmts ::= _stmts (79)
L. 40: 158     expr ::= LOAD_CONST (80)
L. 40: 158     expr ::= LOAD_CONST (80)
L. 40: 158     return_expr ::= expr (80)
L. 40: 158     return_expr ::= expr (80)
       160     expr ::= LOAD_FAST (81)
               store ::= expr STORE_ATTR (82)
               assign ::= expr store (82)
               stmt ::= assign (82)
               stmts ::= stmts stmt (82)
               stmts ::= stmt (82)
               sstmt ::= stmt (82)
               c_stmt ::= stmt (82)
               stmts ::= stmts stmt (82)
               stmts ::= stmts stmt (82)
               stmts ::= stmts stmt (82)
               stmts ::= stmts stmt (82)
               stmts ::= stmts stmt (82)
               stmts ::= stmts stmt (82)
               stmts ::= stmts stmt (82)
               stmts ::= stmts stmt (82)
               stmts ::= stmts stmt (82)
               START ::= |- stmts (82)
               _stmts ::= stmts (82)
               _stmts ::= stmts (82)
               stmts ::= stmts sstmt (82)
               stmts ::= sstmt (82)
               stmts ::= stmts sstmt (82)
               stmts ::= stmts sstmt (82)
               stmts ::= stmts sstmt (82)
               stmts ::= stmts sstmt (82)
               stmts ::= stmts sstmt (82)
               stmts ::= stmts sstmt (82)
               stmts ::= stmts sstmt (82)
               stmts ::= stmts sstmt (82)
               stmts ::= stmts sstmt (82)
               c_stmts ::= c_stmt (82)
               c_stmts ::= c_stmts c_stmt (82)
               c_stmts ::= c_stmts c_stmt (82)
               c_stmts ::= c_stmts c_stmt (82)
               c_stmts ::= c_stmts c_stmt (82)
               c_stmts ::= c_stmts c_stmt (82)
               c_stmts ::= c_stmts c_stmt (82)
               c_stmts ::= c_stmts c_stmt (82)
               c_stmts ::= c_stmts c_stmt (82)
               c_stmts ::= c_stmts c_stmt (82)
               c_stmts ::= c_stmts c_stmt (82)
               _stmts ::= stmts (82)
               _stmts ::= stmts (82)
               _stmts ::= stmts (82)
               _stmts ::= stmts (82)
               _stmts ::= stmts (82)
               _stmts ::= stmts (82)
               _stmts ::= stmts (82)
               _stmts ::= stmts (82)
               _stmts ::= stmts (82)
               c_stmts ::= _stmts (82)
               c_stmts ::= _stmts (82)
               c_stmts ::= _stmts (82)
               c_stmts ::= _stmts (82)
               c_stmts ::= _stmts (82)
               c_stmts ::= _stmts (82)
               c_stmts ::= _stmts (82)
               c_stmts ::= _stmts (82)
               c_stmts ::= _stmts (82)
               c_stmts ::= _stmts (82)
               c_stmts ::= _stmts (82)
               expr ::= LOAD_FAST (1)
               return_expr ::= expr (1)
               attribute37 ::= expr LOAD_METHOD (2)
               expr ::= attribute37 (2)
               return_expr ::= expr (2)
               call ::= expr CALL_METHOD_0 (3)
               expr ::= call (3)
               return_expr ::= expr (3)
               expr_stmt ::= expr POP_TOP (4)
               stmt ::= expr_stmt (4)
               stmts ::= stmt (4)
               sstmt ::= stmt (4)
               c_stmt ::= stmt (4)
               START ::= |- stmts (4)
               _stmts ::= stmts (4)
               stmts ::= sstmt (4)
               c_stmts ::= c_stmt (4)
               c_stmts ::= _stmts (4)
L. 44:   8     expr ::= LOAD_FAST (5)
L. 44:   8     return_expr ::= expr (5)
L. 44:   8     return_expr ::= expr (5)
L. 44:   8-10  attribute ::= expr LOAD_ATTR (6)
L. 44:   8     expr ::= attribute (6)
L. 44:   8     return_expr ::= expr (6)
L. 44:   8     return_expr ::= expr (6)
L. 44:   8-12  attribute37 ::= expr LOAD_METHOD (7)
L. 44:   8     expr ::= attribute37 (7)
L. 44:   8     return_expr ::= expr (7)
L. 44:   8     return_expr ::= expr (7)
        14     expr ::= LOAD_FAST (8)
        14-16  attribute ::= expr LOAD_ATTR (9)
        14     expr ::= attribute (9)
        18     expr ::= LOAD_FAST (10)
        18-20  attribute ::= expr LOAD_ATTR (11)
        18     expr ::= attribute (11)
        18-22  attribute ::= expr LOAD_ATTR (12)
        18     expr ::= attribute (12)
L. 44:   8-24  call ::= expr expr expr CALL_METHOD_2 (13)
L. 44:   8     expr ::= call (13)
L. 44:   8     return_expr ::= expr (13)
L. 44:   8     return_expr ::= expr (13)
               expr_stmt ::= expr POP_TOP (14)
               stmt ::= expr_stmt (14)
               stmts ::= stmts stmt (14)
               stmts ::= stmt (14)
               sstmt ::= stmt (14)
               c_stmt ::= stmt (14)
               START ::= |- stmts (14)
               _stmts ::= stmts (14)
               _stmts ::= stmts (14)
               stmts ::= stmts sstmt (14)
               stmts ::= sstmt (14)
               c_stmts ::= c_stmt (14)
               c_stmts ::= c_stmts c_stmt (14)
               c_stmts ::= _stmts (14)
               c_stmts ::= _stmts (14)
               expr ::= LOAD_FAST (1)
               return_expr ::= expr (1)
         2     expr ::= LOAD_FAST (2)
         2-4   store ::= expr STORE_ATTR (3)
               assign ::= expr store (3)
               stmt ::= assign (3)
               stmts ::= stmt (3)
               sstmt ::= stmt (3)
               c_stmt ::= stmt (3)
               START ::= |- stmts (3)
               _stmts ::= stmts (3)
               stmts ::= sstmt (3)
               c_stmts ::= c_stmt (3)
               c_stmts ::= _stmts (3)
L. 48:   6     expr ::= LOAD_FAST (4)
L. 48:   6     return_expr ::= expr (4)
L. 48:   6     return_expr ::= expr (4)
         8     expr ::= LOAD_FAST (5)
               store ::= expr STORE_ATTR (6)
               assign ::= expr store (6)
               stmt ::= assign (6)
               stmts ::= stmts stmt (6)
               stmts ::= stmt (6)
               sstmt ::= stmt (6)
               c_stmt ::= stmt (6)
               START ::= |- stmts (6)
               _stmts ::= stmts (6)
               _stmts ::= stmts (6)
               stmts ::= stmts sstmt (6)
               stmts ::= sstmt (6)
               c_stmts ::= c_stmt (6)
               c_stmts ::= c_stmts c_stmt (6)
               c_stmts ::= _stmts (6)
               c_stmts ::= _stmts (6)
               expr ::= LOAD_FAST (1)
               return_expr ::= expr (1)
         2     expr ::= LOAD_FAST (2)
               store ::= expr STORE_ATTR (3)
               assign ::= expr store (3)
               stmt ::= assign (3)
               stmts ::= stmt (3)
               sstmt ::= stmt (3)
               c_stmt ::= stmt (3)
               START ::= |- stmts (3)
               _stmts ::= stmts (3)
               stmts ::= sstmt (3)
               c_stmts ::= c_stmt (3)
               c_stmts ::= _stmts (3)
               expr ::= LOAD_FAST (1)
               return_expr ::= expr (1)
               attribute ::= expr LOAD_ATTR (2)
               expr ::= attribute (2)
               return_expr ::= expr (2)
               return ::= return_expr RETURN_VALUE (3)
               stmt ::= return (3)
               returns ::= return (3)
               stmts ::= stmt (3)
               sstmt ::= stmt (3)
               c_stmt ::= stmt (3)
               c_returns ::= returns (3)
               START ::= |- stmts (3)
               _stmts ::= stmts (3)
               stmts ::= sstmt (3)
               c_stmts ::= c_stmt (3)
               c_stmts ::= c_returns (3)
               c_stmts ::= _stmts (3)
               sstmt ::= return RETURN_LAST (4)
               sstmt ::= sstmt RETURN_LAST (4)
               stmts ::= sstmt (4)
               START ::= |- stmts (4)
               _stmts ::= stmts (4)
               c_stmts ::= _stmts (4)
               expr ::= LOAD_FAST (1)
               return_expr ::= expr (1)
               attribute ::= expr LOAD_ATTR (2)
               expr ::= attribute (2)
               return_expr ::= expr (2)
               expr_pjit ::= expr POP_JUMP_IF_TRUE (3)
               testtrue ::= expr_pjit (3)
               not ::= expr_pjit (3)
               or_parts ::= expr_pjit (3)
               testexpr ::= testtrue (3)
               expr ::= not (3)
               testexprc ::= testexpr (3)
               return_expr ::= expr (3)
L. 58:   6     expr ::= LOAD_CONST (4)
L. 58:   6     expr ::= LOAD_CONST (4)
               or_in_ifexp ::= expr_pjit expr (4)
               or ::= or_parts expr (4)
Reduce or invalid by check
L. 58:   6     return_expr ::= expr (4)
L. 58:   6-8   return ::= return_expr RETURN_VALUE (5)
L. 58:   6     returns ::= return (5)
L. 58:   6     stmt ::= return (5)
               iflaststmt ::= testexpr returns (5)
Reduce iflaststmt invalid by check
L. 58:   6     c_returns ::= returns (5)
L. 58:   6     stmts ::= stmt (5)
L. 58:   6     c_stmt ::= stmt (5)
L. 58:   6     sstmt ::= stmt (5)
L. 58:   6     c_stmts ::= c_returns (5)
               ifstmt ::= testexpr stmts \e__come_froms (5)
               iflaststmt ::= testexpr stmts (5)
Reduce iflaststmt invalid by check
L. 58:   6     stmts_opt ::= stmts (5)
L. 58:   6     _stmts ::= stmts (5)
L. 58:   6     c_stmts ::= c_stmt (5)
L. 58:   6     stmts ::= sstmt (5)
               iflaststmtc ::= testexpr c_stmts (5)
Reduce iflaststmtc invalid by check
L. 58:   6     c_stmts_opt ::= c_stmts (5)
L. 58:   6     ifstmts_jumpc ::= c_stmts (5)
               iflaststmtc ::= testexprc c_stmts (5)
Reduce iflaststmtc invalid by check
               stmt ::= ifstmt (5)
L. 58:   6     c_stmts ::= _stmts (5)
               ifstmtc ::= testexpr ifstmts_jumpc (5)
               ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms (5)
               if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms (5)
Reduce if_not_stmtc invalid by check
               stmts ::= stmt (5)
               c_stmt ::= stmt (5)
               sstmt ::= stmt (5)
               c_stmt ::= ifstmtc (5)
               START ::= |- stmts (5)
               _stmts ::= stmts (5)
               c_stmts ::= c_stmt (5)
               stmts ::= sstmt (5)
               c_stmts ::= _stmts (5)
        10-10  _come_froms ::= \e__come_froms COME_FROM (6)
        10     come_froms ::= COME_FROM (6)
        10-10  _come_froms ::= \e__come_froms COME_FROM (6)
        10     come_froms ::= COME_FROM (6)
        10     come_froms ::= COME_FROM (6)
        10     come_from_opt ::= COME_FROM (6)
        10     come_froms ::= COME_FROM (6)
               ifstmt ::= testexpr stmts _come_froms (6)
               ifstmtc ::= testexprc ifstmts_jumpc _come_froms (6)
               if_not_stmtc ::= testexprc ifstmts_jumpc _come_froms (6)
Reduce if_not_stmtc invalid by check
L. 58:   6-10  ifstmts_jump ::= stmts come_froms (6)
               whilestmt38 ::= \e__come_froms testexpr c_stmts come_froms (6)
Reduce whilestmt38 invalid by check
               iflaststmtc ::= testexpr c_stmts come_froms (6)
Reduce iflaststmtc invalid by check
L. 58:   6-10  ifstmts_jump ::= stmts_opt come_froms (6)
L. 58:   6-10  ifstmts_jumpc ::= c_stmts_opt come_froms (6)
               stmt ::= ifstmt (6)
               c_stmt ::= ifstmtc (6)
               ifstmt ::= testexpr ifstmts_jump \e__come_froms (6)
L. 58:   6     ifstmts_jumpc ::= ifstmts_jump (6)
               ifstmtc ::= testexpr ifstmts_jumpc (6)
               ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms (6)
               if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms (6)
Reduce if_not_stmtc invalid by check
               stmts ::= stmt (6)
               c_stmt ::= stmt (6)
               sstmt ::= stmt (6)
               c_stmts ::= c_stmt (6)
               START ::= |- stmts (6)
               _stmts ::= stmts (6)
               stmts ::= sstmt (6)
               c_stmts ::= _stmts (6)
L. 60:  10     expr ::= LOAD_CONST (7)
L. 60:  10     expr ::= LOAD_CONST (7)
L. 60:  10     return_expr ::= expr (7)
L. 60:  10     return_expr ::= expr (7)
        12     store ::= STORE_FAST (8)
L. 60:  10-12  assign ::= expr store (8)
L. 60:  10     stmt ::= assign (8)
L. 60:  10     stmts ::= stmt (8)
L. 60:  10     c_stmt ::= stmt (8)
L. 60:  10     sstmt ::= stmt (8)
               stmts ::= stmts stmt (8)
L. 60:  10     _stmts ::= stmts (8)
L. 60:  10     c_stmts ::= c_stmt (8)
               c_stmts ::= c_stmts c_stmt (8)
L. 60:  10     stmts ::= sstmt (8)
               stmts ::= stmts sstmt (8)
               START ::= |- stmts (8)
               _stmts ::= stmts (8)
L. 60:  10     c_stmts ::= _stmts (8)
L. 60:  10     suite_stmts ::= _stmts (8)
L. 60:  10     c_stmts ::= _stmts (8)
               c_stmts ::= _stmts (8)
L. 60:  10     else_suite ::= suite_stmts (8)
               ifelsestmtc ::= testexpr c_stmts come_froms else_suite (8)
               lastc_stmt ::= ifelsestmtc (8)
Reduce lastc_stmt invalid by check
               c_stmt ::= ifelsestmtc (8)
               c_stmts ::= c_stmt (8)
L. 62:  14     expr ::= LOAD_CONST (9)
L. 62:  14     expr ::= LOAD_CONST (9)
L. 62:  14     return_expr ::= expr (9)
L. 62:  14     return_expr ::= expr (9)
        16     store ::= STORE_FAST (10)
L. 62:  14-16  assign ::= expr store (10)
L. 62:  14     stmt ::= assign (10)
L. 60:  10-16  stmts ::= stmts stmt (10)
L. 62:  14     stmts ::= stmt (10)
L. 62:  14     c_stmt ::= stmt (10)
L. 62:  14     sstmt ::= stmt (10)
               stmts ::= stmts stmt (10)
L. 60:  10     _stmts ::= stmts (10)
L. 62:  14     _stmts ::= stmts (10)
L. 62:  14     c_stmts ::= c_stmt (10)
L. 60:  10-16  c_stmts ::= c_stmts c_stmt (10)
               c_stmts ::= c_stmts c_stmt (10)
L. 60:  10-16  stmts ::= stmts sstmt (10)
L. 62:  14     stmts ::= sstmt (10)
               stmts ::= stmts sstmt (10)
               START ::= |- stmts (10)
               _stmts ::= stmts (10)
L. 60:  10     c_stmts ::= _stmts (10)
L. 60:  10     suite_stmts ::= _stmts (10)
L. 60:  10     c_stmts ::= _stmts (10)
L. 62:  14     c_stmts ::= _stmts (10)
               c_stmts ::= _stmts (10)
L. 60:  10     else_suite ::= suite_stmts (10)
               ifelsestmtc ::= testexpr c_stmts come_froms else_suite (10)
               lastc_stmt ::= ifelsestmtc (10)
Reduce lastc_stmt invalid by check
               c_stmt ::= ifelsestmtc (10)
               c_stmts ::= c_stmt (10)
L. 63:  18     expr ::= LOAD_CONST (11)
L. 63:  18     expr ::= LOAD_CONST (11)
L. 63:  18     return_expr ::= expr (11)
L. 63:  18     return_expr ::= expr (11)
        20     store ::= STORE_FAST (12)
L. 63:  18-20  assign ::= expr store (12)
L. 63:  18     stmt ::= assign (12)
L. 60:  10-20  stmts ::= stmts stmt (12)
L. 63:  18     stmts ::= stmt (12)
L. 63:  18     c_stmt ::= stmt (12)
L. 63:  18     sstmt ::= stmt (12)
L. 62:  14-20  stmts ::= stmts stmt (12)
               stmts ::= stmts stmt (12)
L. 60:  10     _stmts ::= stmts (12)
L. 63:  18     _stmts ::= stmts (12)
L. 63:  18     c_stmts ::= c_stmt (12)
L. 62:  14-20  c_stmts ::= c_stmts c_stmt (12)
L. 60:  10-20  c_stmts ::= c_stmts c_stmt (12)
               c_stmts ::= c_stmts c_stmt (12)
L. 60:  10-20  stmts ::= stmts sstmt (12)
L. 63:  18     stmts ::= sstmt (12)
L. 62:  14-20  stmts ::= stmts sstmt (12)
               stmts ::= stmts sstmt (12)
L. 62:  14     _stmts ::= stmts (12)
               START ::= |- stmts (12)
               _stmts ::= stmts (12)
L. 60:  10     c_stmts ::= _stmts (12)
L. 60:  10     suite_stmts ::= _stmts (12)
L. 60:  10     c_stmts ::= _stmts (12)
L. 63:  18     c_stmts ::= _stmts (12)
L. 62:  14     c_stmts ::= _stmts (12)
               c_stmts ::= _stmts (12)
L. 60:  10     else_suite ::= suite_stmts (12)
               ifelsestmtc ::= testexpr c_stmts come_froms else_suite (12)
               lastc_stmt ::= ifelsestmtc (12)
Reduce lastc_stmt invalid by check
               c_stmt ::= ifelsestmtc (12)
               c_stmts ::= c_stmt (12)
        24-24  _come_froms ::= \e__come_froms COME_FROM (14)
        24-24  _come_froms ::= _come_froms COME_FROM (15)
        24-24  _come_froms ::= \e__come_froms COME_FROM (15)
        24-24  _come_froms ::= _come_froms COME_FROM (16)
        24-24  _come_froms ::= \e__come_froms COME_FROM (16)
        24-24  _come_froms ::= _come_froms COME_FROM (16)
L. 66:  24     expr ::= LOAD_FAST (17)
L. 66:  24     return_expr ::= expr (17)
L. 66:  24-26  expr_pjif ::= expr POP_JUMP_IF_FALSE (18)
L. 66:  24     testfalse ::= expr_pjif (18)
L. 66:  24     and_parts ::= expr_pjif (18)
L. 66:  24     testexpr ::= testfalse (18)
L. 66:  24     testexprc ::= testexpr (18)
L. 69:  28     expr ::= LOAD_FAST (19)
L. 69:  28     return_expr ::= expr (19)
L. 69:  28-30  expr_pjif ::= expr POP_JUMP_IF_FALSE (20)
L. 69:  28-30  expr_pjif ::= expr POP_JUMP_IF_FALSE (20)
L. 69:  28     and_parts ::= expr_pjif (20)
L. 69:  28     testfalse ::= expr_pjif (20)
L. 66:  24-30  and_cond ::= testfalse expr_pjif \e__come_froms (20)
Reduce and_cond invalid by check
L. 66:  24-30  and_cond ::= and_parts expr_pjif \e__come_froms (20)
Reduce and_cond invalid by check
L. 66:  24-30  not_or ::= and_parts expr_pjif \e__come_froms (20)
Reduce not_or invalid by check
L. 66:  24-30  and_parts ::= and_parts expr_pjif (20)
L. 69:  28     testfalse ::= expr_pjif (20)
L. 69:  28     and_parts ::= expr_pjif (20)
L. 69:  28     testexpr ::= testfalse (20)
L. 69:  28     testexprc ::= testexpr (20)
        32     expr ::= LOAD_FAST (21)
        32     return_expr ::= expr (21)
        34     expr ::= LOAD_GLOBAL (22)
        32-36  compare_single ::= expr expr COMPARE_OP (23)
        32     compare ::= compare_single (23)
        32     expr ::= compare (23)
        32     return_expr ::= expr (23)
        32-38  expr_pjif ::= expr POP_JUMP_IF_FALSE (24)
        32-38  expr_pjif ::= expr POP_JUMP_IF_FALSE (24)
        32     testfalse ::= expr_pjif (24)
        32     and_parts ::= expr_pjif (24)
        32     and_parts ::= expr_pjif (24)
        32     testfalse ::= expr_pjif (24)
L. 69:  28-38  and_cond ::= and_parts expr_pjif \e__come_froms (24)
L. 69:  28-38  not_or ::= and_parts expr_pjif \e__come_froms (24)
Reduce not_or invalid by check
L. 69:  28-38  and_parts ::= and_parts expr_pjif (24)
L. 69:  28-38  and_cond ::= testfalse expr_pjif \e__come_froms (24)
L. 66:  24-38  and_cond ::= and_parts expr_pjif \e__come_froms (24)
Reduce and_cond invalid by check
L. 66:  24-38  not_or ::= and_parts expr_pjif \e__come_froms (24)
Reduce not_or invalid by check
L. 66:  24-38  and_parts ::= and_parts expr_pjif (24)
        32     testexpr ::= testfalse (24)
L. 69:  28     bool_op ::= and_cond (24)
        32     testexprc ::= testexpr (24)
L. 70:  40     expr ::= LOAD_GLOBAL (25)
L. 70:  40     return_expr ::= expr (25)
L. 70:  40-42  attribute37 ::= expr LOAD_METHOD (26)
L. 70:  40     expr ::= attribute37 (26)
L. 70:  40     return_expr ::= expr (26)
        44     expr ::= LOAD_STR (27)
L. 71:  46     expr ::= LOAD_STR (28)
        48     expr ::= LOAD_GLOBAL (29)
        50     binary_operator ::= BINARY_MODULO (30)
L. 71:  46-50  bin_op ::= expr expr binary_operator (30)
L. 71:  46     expr ::= bin_op (30)
L. 70:  52     binary_operator ::= BINARY_ADD (31)
        44-52  bin_op ::= expr expr binary_operator (31)
        44     expr ::= bin_op (31)
L. 70:  40-54  call ::= expr expr CALL_METHOD_1 (32)
L. 70:  40     expr ::= call (32)
L. 70:  40     return_expr ::= expr (32)
L. 70:  40-56  expr_stmt ::= expr POP_TOP (33)
L. 70:  40     stmt ::= expr_stmt (33)
L. 70:  40     stmts ::= stmt (33)
L. 70:  40     c_stmt ::= stmt (33)
L. 70:  40     sstmt ::= stmt (33)
L. 70:  40     _stmts ::= stmts (33)
        32-56  ifstmt ::= testexpr stmts \e__come_froms (33)
Reduce ifstmt invalid by check
        32-56  iflaststmt ::= testexpr stmts (33)
Reduce iflaststmt invalid by check
L. 70:  40     stmts_opt ::= stmts (33)
L. 70:  40     _stmts ::= stmts (33)
L. 69:  28-56  ifstmt ::= bool_op stmts \e__come_froms (33)
L. 70:  40     stmts_opt ::= stmts (33)
L. 70:  40     _stmts ::= stmts (33)
L. 70:  40     c_stmts ::= c_stmt (33)
L. 70:  40     stmts ::= sstmt (33)
L. 70:  40     c_stmts ::= _stmts (33)
L. 70:  40     c_stmts ::= _stmts (33)
L. 69:  28     stmt ::= ifstmt (33)
        32-56  iflaststmtc ::= testexpr c_stmts (33)
Reduce iflaststmtc invalid by check
L. 70:  40     c_stmts_opt ::= c_stmts (33)
L. 70:  40     ifstmts_jumpc ::= c_stmts (33)
        32-56  iflaststmtc ::= testexprc c_stmts (33)
Reduce iflaststmtc invalid by check
L. 69:  28     stmts ::= stmt (33)
L. 69:  28     c_stmt ::= stmt (33)
L. 69:  28     sstmt ::= stmt (33)
        32-56  ifstmtc ::= testexpr ifstmts_jumpc (33)
Reduce ifstmtc invalid by check
        32-56  ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms (33)
Reduce ifstmtc invalid by check
        32-56  if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms (33)
L. 69:  28     _stmts ::= stmts (33)
L. 66:  24-56  ifstmt ::= testexpr stmts \e__come_froms (33)
Reduce ifstmt invalid by check
L. 66:  24-56  iflaststmt ::= testexpr stmts (33)
Reduce iflaststmt invalid by check
L. 69:  28     stmts_opt ::= stmts (33)
L. 69:  28     _stmts ::= stmts (33)
L. 69:  28     c_stmts ::= c_stmt (33)
L. 69:  28     stmts ::= sstmt (33)
        32     c_stmt ::= if_not_stmtc (33)
L. 69:  28     c_stmts ::= _stmts (33)
L. 69:  28     c_stmts ::= _stmts (33)
L. 69:  28     c_stmts_opt ::= c_stmts (33)
L. 66:  24-56  iflaststmtc ::= testexpr c_stmts (33)
Reduce iflaststmtc invalid by check
L. 69:  28     c_stmts_opt ::= c_stmts (33)
L. 69:  28     ifstmts_jumpc ::= c_stmts (33)
L. 66:  24-56  iflaststmtc ::= testexprc c_stmts (33)
Reduce iflaststmtc invalid by check
        32     c_stmts ::= c_stmt (33)
L. 66:  24-56  ifstmtc ::= testexpr ifstmts_jumpc (33)
Reduce ifstmtc invalid by check
L. 66:  24-56  ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms (33)
Reduce ifstmtc invalid by check
L. 66:  24-56  if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms (33)
L. 69:  28-56  iflaststmtc ::= testexpr c_stmts (33)
Reduce iflaststmtc invalid by check
        32     c_stmts_opt ::= c_stmts (33)
        32     ifstmts_jumpc ::= c_stmts (33)
L. 69:  28-56  iflaststmtc ::= testexprc c_stmts (33)
Reduce iflaststmtc invalid by check
L. 66:  24     c_stmt ::= if_not_stmtc (33)
L. 69:  28-56  ifstmtc ::= testexpr ifstmts_jumpc (33)
Reduce ifstmtc invalid by check
L. 69:  28-56  ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms (33)
Reduce ifstmtc invalid by check
L. 69:  28-56  if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms (33)
L. 66:  24     c_stmts ::= c_stmt (33)
L. 69:  28     c_stmt ::= if_not_stmtc (33)
L. 72:  58     expr ::= LOAD_FAST (34)
L. 72:  58     return_expr ::= expr (34)
L. 72:  58     return_expr ::= expr (34)
L. 72:  58-60  attribute37 ::= expr LOAD_METHOD (35)
L. 72:  58     expr ::= attribute37 (35)
L. 72:  58     return_expr ::= expr (35)
L. 72:  58     return_expr ::= expr (35)
L. 72:  58-62  call ::= expr CALL_METHOD_0 (36)
L. 72:  58     expr ::= call (36)
L. 72:  58     return_expr ::= expr (36)
L. 72:  58     return_expr ::= expr (36)
L. 72:  58-64  expr_stmt ::= expr POP_TOP (37)
L. 72:  58     stmt ::= expr_stmt (37)
L. 70:  40-64  stmts ::= stmts stmt (37)
L. 72:  58     stmts ::= stmt (37)
L. 72:  58     c_stmt ::= stmt (37)
L. 72:  58     sstmt ::= stmt (37)
L. 69:  28-64  stmts ::= stmts stmt (37)
L. 70:  40     _stmts ::= stmts (37)
        32-64  ifstmt ::= testexpr stmts \e__come_froms (37)
Reduce ifstmt invalid by check
        32-64  iflaststmt ::= testexpr stmts (37)
Reduce iflaststmt invalid by check
L. 70:  40     stmts_opt ::= stmts (37)
L. 70:  40     _stmts ::= stmts (37)
L. 69:  28-64  ifstmt ::= bool_op stmts \e__come_froms (37)
L. 70:  40     stmts_opt ::= stmts (37)
L. 70:  40     _stmts ::= stmts (37)
L. 72:  58     _stmts ::= stmts (37)
L. 72:  58     c_stmts ::= c_stmt (37)
L. 70:  40-64  c_stmts ::= c_stmts c_stmt (37)
L. 69:  28-64  c_stmts ::= c_stmts c_stmt (37)
        32-64  c_stmts ::= c_stmts c_stmt (37)
L. 66:  24-64  c_stmts ::= c_stmts c_stmt (37)
L. 70:  40-64  stmts ::= stmts sstmt (37)
L. 72:  58     stmts ::= sstmt (37)
L. 69:  28-64  stmts ::= stmts sstmt (37)
L. 69:  28     _stmts ::= stmts (37)
L. 66:  24-64  ifstmt ::= testexpr stmts \e__come_froms (37)
Reduce ifstmt invalid by check
L. 66:  24-64  iflaststmt ::= testexpr stmts (37)
Reduce iflaststmt invalid by check
L. 69:  28     stmts_opt ::= stmts (37)
L. 69:  28     _stmts ::= stmts (37)
L. 70:  40     c_stmts ::= _stmts (37)
L. 70:  40     c_stmts ::= _stmts (37)
L. 69:  28     stmt ::= ifstmt (37)
L. 72:  58     c_stmts ::= _stmts (37)
        32-64  iflaststmtc ::= testexpr c_stmts (37)
Reduce iflaststmtc invalid by check
L. 70:  40     c_stmts_opt ::= c_stmts (37)
L. 70:  40     ifstmts_jumpc ::= c_stmts (37)
        32-64  iflaststmtc ::= testexprc c_stmts (37)
Reduce iflaststmtc invalid by check
L. 69:  28     c_stmts_opt ::= c_stmts (37)
L. 66:  24-64  iflaststmtc ::= testexpr c_stmts (37)
Reduce iflaststmtc invalid by check
L. 69:  28     c_stmts_opt ::= c_stmts (37)
L. 69:  28     ifstmts_jumpc ::= c_stmts (37)
L. 66:  24-64  iflaststmtc ::= testexprc c_stmts (37)
Reduce iflaststmtc invalid by check
L. 69:  28-64  iflaststmtc ::= testexpr c_stmts (37)
Reduce iflaststmtc invalid by check
        32     c_stmts_opt ::= c_stmts (37)
        32     ifstmts_jumpc ::= c_stmts (37)
L. 69:  28-64  iflaststmtc ::= testexprc c_stmts (37)
Reduce iflaststmtc invalid by check
L. 69:  28     c_stmts ::= _stmts (37)
L. 69:  28     c_stmts ::= _stmts (37)
L. 69:  28     stmts ::= stmt (37)
L. 69:  28     c_stmt ::= stmt (37)
L. 69:  28     sstmt ::= stmt (37)
        32-64  ifstmtc ::= testexpr ifstmts_jumpc (37)
Reduce ifstmtc invalid by check
        32-64  ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms (37)
Reduce ifstmtc invalid by check
        32-64  if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms (37)
L. 66:  24-64  ifstmtc ::= testexpr ifstmts_jumpc (37)
Reduce ifstmtc invalid by check
L. 66:  24-64  ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms (37)
Reduce ifstmtc invalid by check
L. 66:  24-64  if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms (37)
L. 69:  28-64  ifstmtc ::= testexpr ifstmts_jumpc (37)
Reduce ifstmtc invalid by check
L. 69:  28-64  ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms (37)
Reduce ifstmtc invalid by check
L. 69:  28-64  if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms (37)
L. 69:  28     c_stmts ::= c_stmt (37)
L. 69:  28     stmts ::= sstmt (37)
        32     c_stmt ::= if_not_stmtc (37)
L. 66:  24     c_stmt ::= if_not_stmtc (37)
L. 69:  28     c_stmt ::= if_not_stmtc (37)
        32     c_stmts ::= c_stmt (37)
L. 66:  24     c_stmts ::= c_stmt (37)
L. 73:  66     expr ::= LOAD_CONST (38)
L. 73:  66     expr ::= LOAD_CONST (38)
L. 73:  66     return_expr ::= expr (38)
L. 73:  66     return_expr ::= expr (38)
        68     store ::= STORE_FAST (39)
L. 73:  66-68  assign ::= expr store (39)
L. 73:  66     stmt ::= assign (39)
L. 70:  40-68  stmts ::= stmts stmt (39)
L. 73:  66     stmts ::= stmt (39)
L. 73:  66     c_stmt ::= stmt (39)
L. 73:  66     sstmt ::= stmt (39)
L. 72:  58-68  stmts ::= stmts stmt (39)
L. 69:  28-68  stmts ::= stmts stmt (39)
L. 70:  40     _stmts ::= stmts (39)
        32-68  ifstmt ::= testexpr stmts \e__come_froms (39)
Reduce ifstmt invalid by check
        32-68  iflaststmt ::= testexpr stmts (39)
Reduce iflaststmt invalid by check
L. 70:  40     stmts_opt ::= stmts (39)
L. 70:  40     _stmts ::= stmts (39)
L. 69:  28-68  ifstmt ::= bool_op stmts \e__come_froms (39)
L. 70:  40     stmts_opt ::= stmts (39)
L. 70:  40     _stmts ::= stmts (39)
L. 73:  66     _stmts ::= stmts (39)
L. 73:  66     c_stmts ::= c_stmt (39)
L. 72:  58-68  c_stmts ::= c_stmts c_stmt (39)
L. 70:  40-68  c_stmts ::= c_stmts c_stmt (39)
L. 69:  28-68  c_stmts ::= c_stmts c_stmt (39)
        32-68  c_stmts ::= c_stmts c_stmt (39)
L. 66:  24-68  c_stmts ::= c_stmts c_stmt (39)
L. 70:  40-68  stmts ::= stmts sstmt (39)
L. 73:  66     stmts ::= sstmt (39)
L. 72:  58-68  stmts ::= stmts sstmt (39)
L. 69:  28-68  stmts ::= stmts sstmt (39)
L. 72:  58     _stmts ::= stmts (39)
L. 69:  28     _stmts ::= stmts (39)
L. 66:  24-68  ifstmt ::= testexpr stmts \e__come_froms (39)
Reduce ifstmt invalid by check
L. 66:  24-68  iflaststmt ::= testexpr stmts (39)
Reduce iflaststmt invalid by check
L. 69:  28     stmts_opt ::= stmts (39)
L. 69:  28     _stmts ::= stmts (39)
L. 70:  40     c_stmts ::= _stmts (39)
L. 70:  40     c_stmts ::= _stmts (39)
L. 69:  28     stmt ::= ifstmt (39)
L. 73:  66     c_stmts ::= _stmts (39)
        32-68  iflaststmtc ::= testexpr c_stmts (39)
Reduce iflaststmtc invalid by check
L. 70:  40     c_stmts_opt ::= c_stmts (39)
L. 70:  40     ifstmts_jumpc ::= c_stmts (39)
        32-68  iflaststmtc ::= testexprc c_stmts (39)
Reduce iflaststmtc invalid by check
L. 69:  28     c_stmts_opt ::= c_stmts (39)
L. 66:  24-68  iflaststmtc ::= testexpr c_stmts (39)
Reduce iflaststmtc invalid by check
L. 69:  28     c_stmts_opt ::= c_stmts (39)
L. 69:  28     ifstmts_jumpc ::= c_stmts (39)
L. 66:  24-68  iflaststmtc ::= testexprc c_stmts (39)
Reduce iflaststmtc invalid by check
L. 69:  28-68  iflaststmtc ::= testexpr c_stmts (39)
Reduce iflaststmtc invalid by check
        32     c_stmts_opt ::= c_stmts (39)
        32     ifstmts_jumpc ::= c_stmts (39)
L. 69:  28-68  iflaststmtc ::= testexprc c_stmts (39)
Reduce iflaststmtc invalid by check
L. 72:  58     c_stmts ::= _stmts (39)
L. 69:  28     c_stmts ::= _stmts (39)
L. 69:  28     c_stmts ::= _stmts (39)
L. 69:  28     stmts ::= stmt (39)
L. 69:  28     c_stmt ::= stmt (39)
L. 69:  28     sstmt ::= stmt (39)
        32-68  ifstmtc ::= testexpr ifstmts_jumpc (39)
Reduce ifstmtc invalid by check
        32-68  ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms (39)
Reduce ifstmtc invalid by check
        32-68  if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms (39)
L. 66:  24-68  ifstmtc ::= testexpr ifstmts_jumpc (39)
Reduce ifstmtc invalid by check
L. 66:  24-68  ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms (39)
Reduce ifstmtc invalid by check
L. 66:  24-68  if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms (39)
L. 69:  28-68  ifstmtc ::= testexpr ifstmts_jumpc (39)
Reduce ifstmtc invalid by check
L. 69:  28-68  ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms (39)
Reduce ifstmtc invalid by check
L. 69:  28-68  if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms (39)
L. 69:  28     c_stmts ::= c_stmt (39)
L. 69:  28     stmts ::= sstmt (39)
        32     c_stmt ::= if_not_stmtc (39)
L. 66:  24     c_stmt ::= if_not_stmtc (39)
L. 69:  28     c_stmt ::= if_not_stmtc (39)
        32     c_stmts ::= c_stmt (39)
L. 66:  24     c_stmts ::= c_stmt (39)
L. 74:  70     break ::= BREAK_LOOP (40)
L. 74:  70     stmt ::= break (40)
L. 74:  70     c_stmt ::= break (40)
L. 70:  40-70  stmts ::= stmts stmt (40)
L. 74:  70     stmts ::= stmt (40)
L. 74:  70     c_stmt ::= stmt (40)
L. 74:  70     sstmt ::= stmt (40)
L. 73:  66-70  stmts ::= stmts stmt (40)
L. 72:  58-70  stmts ::= stmts stmt (40)
L. 69:  28-70  stmts ::= stmts stmt (40)
L. 74:  70     c_stmts ::= c_stmt (40)
L. 73:  66-70  c_stmts ::= c_stmts c_stmt (40)
L. 72:  58-70  c_stmts ::= c_stmts c_stmt (40)
L. 70:  40-70  c_stmts ::= c_stmts c_stmt (40)
L. 69:  28-70  c_stmts ::= c_stmts c_stmt (40)
        32-70  c_stmts ::= c_stmts c_stmt (40)
L. 66:  24-70  c_stmts ::= c_stmts c_stmt (40)
L. 70:  40     _stmts ::= stmts (40)
        32-70  ifstmt ::= testexpr stmts \e__come_froms (40)
        32-70  iflaststmt ::= testexpr stmts (40)
Reduce iflaststmt invalid by check
L. 70:  40     stmts_opt ::= stmts (40)
L. 70:  40     _stmts ::= stmts (40)
L. 69:  28-70  ifstmt ::= bool_op stmts \e__come_froms (40)
L. 70:  40     stmts_opt ::= stmts (40)
L. 70:  40     _stmts ::= stmts (40)
L. 74:  70     _stmts ::= stmts (40)
L. 70:  40-70  stmts ::= stmts sstmt (40)
L. 74:  70     stmts ::= sstmt (40)
L. 73:  66-70  stmts ::= stmts sstmt (40)
L. 72:  58-70  stmts ::= stmts sstmt (40)
L. 69:  28-70  stmts ::= stmts sstmt (40)
L. 73:  66     _stmts ::= stmts (40)
L. 72:  58     _stmts ::= stmts (40)
L. 69:  28     _stmts ::= stmts (40)
L. 66:  24-70  ifstmt ::= testexpr stmts \e__come_froms (40)
L. 66:  24-70  iflaststmt ::= testexpr stmts (40)
Reduce iflaststmt invalid by check
L. 69:  28     stmts_opt ::= stmts (40)
L. 69:  28     _stmts ::= stmts (40)
        32-70  iflaststmtc ::= testexpr c_stmts (40)
Reduce iflaststmtc invalid by check
L. 70:  40     c_stmts_opt ::= c_stmts (40)
L. 70:  40     ifstmts_jumpc ::= c_stmts (40)
        32-70  iflaststmtc ::= testexprc c_stmts (40)
Reduce iflaststmtc invalid by check
L. 69:  28     c_stmts_opt ::= c_stmts (40)
L. 66:  24-70  iflaststmtc ::= testexpr c_stmts (40)
Reduce iflaststmtc invalid by check
L. 69:  28     c_stmts_opt ::= c_stmts (40)
L. 69:  28     ifstmts_jumpc ::= c_stmts (40)
L. 66:  24-70  iflaststmtc ::= testexprc c_stmts (40)
Reduce iflaststmtc invalid by check
L. 69:  28-70  iflaststmtc ::= testexpr c_stmts (40)
Reduce iflaststmtc invalid by check
        32     c_stmts_opt ::= c_stmts (40)
        32     ifstmts_jumpc ::= c_stmts (40)
L. 69:  28-70  iflaststmtc ::= testexprc c_stmts (40)
Reduce iflaststmtc invalid by check
L. 70:  40     c_stmts ::= _stmts (40)
L. 70:  40     c_stmts ::= _stmts (40)
        32     stmt ::= ifstmt (40)
L. 69:  28     stmt ::= ifstmt (40)
L. 74:  70     c_stmts ::= _stmts (40)
L. 73:  66     c_stmts ::= _stmts (40)
L. 72:  58     c_stmts ::= _stmts (40)
L. 69:  28     c_stmts ::= _stmts (40)
L. 69:  28     c_stmts ::= _stmts (40)
L. 66:  24     stmt ::= ifstmt (40)
        32-70  ifstmtc ::= testexpr ifstmts_jumpc (40)
        32-70  ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms (40)
        32-70  if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms (40)
Reduce if_not_stmtc invalid by check
L. 66:  24-70  ifstmtc ::= testexpr ifstmts_jumpc (40)
L. 66:  24-70  ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms (40)
L. 66:  24-70  if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms (40)
L. 69:  28-70  ifstmtc ::= testexpr ifstmts_jumpc (40)
L. 69:  28-70  ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms (40)
L. 69:  28-70  if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms (40)
Reduce if_not_stmtc invalid by check
        32     stmts ::= stmt (40)
        32     c_stmt ::= stmt (40)
        32     sstmt ::= stmt (40)
L. 69:  28     stmts ::= stmt (40)
L. 69:  28     c_stmt ::= stmt (40)
L. 69:  28     sstmt ::= stmt (40)
L. 66:  24     stmts ::= stmt (40)
L. 66:  24     c_stmt ::= stmt (40)
L. 66:  24     sstmt ::= stmt (40)
        32     c_stmt ::= ifstmtc (40)
L. 66:  24     c_stmt ::= ifstmtc (40)
L. 66:  24     c_stmt ::= if_not_stmtc (40)
L. 69:  28     c_stmt ::= ifstmtc (40)
        32     _stmts ::= stmts (40)
L. 69:  28-70  ifstmt ::= testexpr stmts \e__come_froms (40)
L. 69:  28-70  iflaststmt ::= testexpr stmts (40)
Reduce iflaststmt invalid by check
        32     stmts_opt ::= stmts (40)
        32     _stmts ::= stmts (40)
        32     c_stmts ::= c_stmt (40)
        32     stmts ::= sstmt (40)
L. 69:  28     c_stmts ::= c_stmt (40)
L. 69:  28     stmts ::= sstmt (40)
L. 66:  24     _stmts ::= stmts (40)
L. 66:  24     c_stmts ::= c_stmt (40)
L. 66:  24     stmts ::= sstmt (40)
        32     c_stmts ::= _stmts (40)
        32     c_stmts ::= _stmts (40)
L. 66:  24     c_stmts ::= _stmts (40)
        72-72  _come_froms ::= \e__come_froms COME_FROM (41)
        72     come_froms ::= COME_FROM (41)
        72-72  _come_froms ::= \e__come_froms COME_FROM (41)
        72     come_from_opt ::= COME_FROM (41)
        72     come_froms ::= COME_FROM (41)
        72     come_froms ::= COME_FROM (41)
        72     come_from_opt ::= COME_FROM (41)
        72     come_froms ::= COME_FROM (41)
        32-72  ifstmt ::= testexpr stmts _come_froms (41)
Reduce ifstmt invalid by check
L. 69:  28-72  ifstmt ::= bool_op stmts _come_froms (41)
L. 66:  24-72  ifstmt ::= testexpr stmts _come_froms (41)
Reduce ifstmt invalid by check
        32-72  ifstmtc ::= testexprc ifstmts_jumpc _come_froms (41)
Reduce ifstmtc invalid by check
        32-72  if_not_stmtc ::= testexprc ifstmts_jumpc _come_froms (41)
Reduce if_not_stmtc invalid by check
L. 66:  24-72  ifstmtc ::= testexprc ifstmts_jumpc _come_froms (41)
Reduce ifstmtc invalid by check
L. 66:  24-72  if_not_stmtc ::= testexprc ifstmts_jumpc _come_froms (41)
L. 69:  28-72  ifstmtc ::= testexprc ifstmts_jumpc _come_froms (41)
L. 69:  28-72  if_not_stmtc ::= testexprc ifstmts_jumpc _come_froms (41)
Reduce if_not_stmtc invalid by check
L. 69:  28-72  ifstmt ::= testexpr stmts _come_froms (41)
L. 70:  40-72  ifstmts_jump ::= stmts come_froms (41)
L. 69:  28-72  ifstmts_jump ::= stmts come_froms (41)
        32-72  whilestmt38 ::= \e__come_froms testexpr c_stmts come_froms (41)
Reduce whilestmt38 invalid by check
        32-72  iflaststmtc ::= testexpr c_stmts come_froms (41)
Reduce iflaststmtc invalid by check
        24-72  whilestmt38 ::= _come_froms testexpr c_stmts come_froms (41)
Reduce whilestmt38 invalid by check
L. 66:  24-72  whilestmt38 ::= \e__come_froms testexpr c_stmts come_froms (41)
Reduce whilestmt38 invalid by check
L. 66:  24-72  iflaststmtc ::= testexpr c_stmts come_froms (41)
Reduce iflaststmtc invalid by check
        24-72  whilestmt38 ::= _come_froms testexpr c_stmts come_froms (41)
Reduce whilestmt38 invalid by check
        24-72  whilestmt38 ::= _come_froms testexpr c_stmts come_froms (41)
Reduce whilestmt38 invalid by check
L. 69:  28-72  whilestmt38 ::= \e__come_froms testexpr c_stmts come_froms (41)
Reduce whilestmt38 invalid by check
L. 69:  28-72  iflaststmtc ::= testexpr c_stmts come_froms (41)
Reduce iflaststmtc invalid by check
L. 70:  40-72  ifstmts_jump ::= stmts_opt come_froms (41)
L. 69:  28-72  ifstmts_jump ::= stmts_opt come_froms (41)
L. 70:  40-72  ifstmts_jumpc ::= c_stmts_opt come_froms (41)
L. 69:  28-72  ifstmts_jumpc ::= c_stmts_opt come_froms (41)
        32-72  ifstmts_jumpc ::= c_stmts_opt come_froms (41)
        32-72  ifstmts_jump ::= stmts come_froms (41)
        32-72  ifstmts_jump ::= stmts_opt come_froms (41)
L. 69:  28     stmt ::= ifstmt (41)
L. 66:  24     c_stmt ::= if_not_stmtc (41)
L. 69:  28     c_stmt ::= ifstmtc (41)
        32-72  ifstmt ::= testexpr ifstmts_jump \e__come_froms (41)
Reduce ifstmt invalid by check
L. 70:  40     ifstmts_jumpc ::= ifstmts_jump (41)
L. 66:  24-72  ifstmt ::= testexpr ifstmts_jump \e__come_froms (41)
Reduce ifstmt invalid by check
L. 69:  28     ifstmts_jumpc ::= ifstmts_jump (41)
        32-72  ifstmtc ::= testexpr ifstmts_jumpc (41)
Reduce ifstmtc invalid by check
        32-72  ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms (41)
Reduce ifstmtc invalid by check
        32-72  if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms (41)
Reduce if_not_stmtc invalid by check
L. 66:  24-72  ifstmtc ::= testexpr ifstmts_jumpc (41)
Reduce ifstmtc invalid by check
L. 66:  24-72  ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms (41)
Reduce ifstmtc invalid by check
L. 66:  24-72  if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms (41)
L. 69:  28-72  ifstmtc ::= testexpr ifstmts_jumpc (41)
L. 69:  28-72  ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms (41)
L. 69:  28-72  if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms (41)
Reduce if_not_stmtc invalid by check
L. 69:  28-72  ifstmt ::= testexpr ifstmts_jump \e__come_froms (41)
        32     ifstmts_jumpc ::= ifstmts_jump (41)
L. 69:  28     stmts ::= stmt (41)
L. 69:  28     c_stmt ::= stmt (41)
L. 69:  28     sstmt ::= stmt (41)
L. 66:  24     c_stmts ::= c_stmt (41)
L. 69:  28     c_stmts ::= c_stmt (41)
L. 69:  28     _stmts ::= stmts (41)
L. 66:  24-72  ifstmt ::= testexpr stmts \e__come_froms (41)
Reduce ifstmt invalid by check
L. 66:  24-72  iflaststmt ::= testexpr stmts (41)
Reduce iflaststmt invalid by check
L. 69:  28     stmts_opt ::= stmts (41)
L. 69:  28     _stmts ::= stmts (41)
L. 69:  28     stmts ::= sstmt (41)
L. 69:  28     c_stmts_opt ::= c_stmts (41)
L. 66:  24-72  iflaststmtc ::= testexpr c_stmts (41)
Reduce iflaststmtc invalid by check
L. 69:  28     c_stmts_opt ::= c_stmts (41)
L. 69:  28     ifstmts_jumpc ::= c_stmts (41)
L. 66:  24-72  iflaststmtc ::= testexprc c_stmts (41)
Reduce iflaststmtc invalid by check
L. 69:  28     c_stmts ::= _stmts (41)
L. 69:  28     c_stmts ::= _stmts (41)
        72-72  _come_froms ::= _come_froms COME_FROM (42)
        72-72  _come_froms ::= \e__come_froms COME_FROM (42)
        72-72  come_froms ::= come_froms COME_FROM (42)
        72     come_froms ::= COME_FROM (42)
        72-72  _come_froms ::= \e__come_froms COME_FROM (42)
        72     come_froms ::= COME_FROM (42)
        72     come_froms ::= COME_FROM (42)
        72     come_from_opt ::= COME_FROM (42)
        72     come_froms ::= COME_FROM (42)
        32-72  ifstmt ::= testexpr stmts _come_froms (42)
L. 69:  28-72  ifstmt ::= bool_op stmts _come_froms (42)
L. 66:  24-72  ifstmt ::= testexpr stmts _come_froms (42)
Reduce ifstmt invalid by check
        32-72  ifstmtc ::= testexprc ifstmts_jumpc _come_froms (42)
        32-72  if_not_stmtc ::= testexprc ifstmts_jumpc _come_froms (42)
Reduce if_not_stmtc invalid by check
L. 66:  24-72  ifstmtc ::= testexprc ifstmts_jumpc _come_froms (42)
Reduce ifstmtc invalid by check
L. 66:  24-72  if_not_stmtc ::= testexprc ifstmts_jumpc _come_froms (42)
L. 69:  28-72  ifstmtc ::= testexprc ifstmts_jumpc _come_froms (42)
L. 69:  28-72  if_not_stmtc ::= testexprc ifstmts_jumpc _come_froms (42)
Reduce if_not_stmtc invalid by check
L. 69:  28-72  ifstmt ::= testexpr stmts _come_froms (42)
        32-72  ifstmt ::= testexpr ifstmts_jump _come_froms (42)
L. 66:  24-72  ifstmt ::= testexpr ifstmts_jump _come_froms (42)
Reduce ifstmt invalid by check
L. 69:  28-72  ifstmt ::= testexpr ifstmts_jump _come_froms (42)
L. 70:  40-72  ifstmts_jump ::= stmts come_froms (42)
Reduce ifstmts_jump invalid by check
L. 69:  28-72  ifstmts_jump ::= stmts come_froms (42)
        32-72  whilestmt38 ::= \e__come_froms testexpr c_stmts come_froms (42)
Reduce whilestmt38 invalid by check
        32-72  iflaststmtc ::= testexpr c_stmts come_froms (42)
Reduce iflaststmtc invalid by check
        24-72  whilestmt38 ::= _come_froms testexpr c_stmts come_froms (42)
Reduce whilestmt38 invalid by check
L. 66:  24-72  whilestmt38 ::= \e__come_froms testexpr c_stmts come_froms (42)
Reduce whilestmt38 invalid by check
L. 66:  24-72  iflaststmtc ::= testexpr c_stmts come_froms (42)
Reduce iflaststmtc invalid by check
        24-72  whilestmt38 ::= _come_froms testexpr c_stmts come_froms (42)
Reduce whilestmt38 invalid by check
        24-72  whilestmt38 ::= _come_froms testexpr c_stmts come_froms (42)
Reduce whilestmt38 invalid by check
L. 69:  28-72  whilestmt38 ::= \e__come_froms testexpr c_stmts come_froms (42)
Reduce whilestmt38 invalid by check
L. 69:  28-72  iflaststmtc ::= testexpr c_stmts come_froms (42)
Reduce iflaststmtc invalid by check
L. 70:  40-72  ifstmts_jump ::= stmts_opt come_froms (42)
Reduce ifstmts_jump invalid by check
L. 69:  28-72  ifstmts_jump ::= stmts_opt come_froms (42)
L. 70:  40-72  ifstmts_jumpc ::= c_stmts_opt come_froms (42)
L. 69:  28-72  ifstmts_jumpc ::= c_stmts_opt come_froms (42)
        32-72  ifstmts_jumpc ::= c_stmts_opt come_froms (42)
        32-72  ifstmts_jump ::= stmts come_froms (42)
        32-72  ifstmts_jump ::= stmts_opt come_froms (42)
        32     stmt ::= ifstmt (42)
L. 69:  28     stmt ::= ifstmt (42)
        32     c_stmt ::= ifstmtc (42)
L. 66:  24     c_stmt ::= if_not_stmtc (42)
L. 69:  28     c_stmt ::= ifstmtc (42)
L. 66:  24-72  ifstmt ::= testexpr ifstmts_jump \e__come_froms (42)
Reduce ifstmt invalid by check
L. 69:  28     ifstmts_jumpc ::= ifstmts_jump (42)
        32-72  ifstmtc ::= testexpr ifstmts_jumpc (42)
        32-72  ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms (42)
        32-72  if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms (42)
Reduce if_not_stmtc invalid by check
L. 66:  24-72  ifstmtc ::= testexpr ifstmts_jumpc (42)
Reduce ifstmtc invalid by check
L. 66:  24-72  ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms (42)
Reduce ifstmtc invalid by check
L. 66:  24-72  if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms (42)
L. 69:  28-72  ifstmtc ::= testexpr ifstmts_jumpc (42)
L. 69:  28-72  ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms (42)
L. 69:  28-72  if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms (42)
Reduce if_not_stmtc invalid by check
L. 69:  28-72  ifstmt ::= testexpr ifstmts_jump \e__come_froms (42)
        32     ifstmts_jumpc ::= ifstmts_jump (42)
        32     stmts ::= stmt (42)
        32     c_stmt ::= stmt (42)
        32     sstmt ::= stmt (42)
L. 69:  28     stmts ::= stmt (42)
L. 69:  28     c_stmt ::= stmt (42)
L. 69:  28     sstmt ::= stmt (42)
        32     c_stmts ::= c_stmt (42)
L. 66:  24     c_stmts ::= c_stmt (42)
L. 69:  28     c_stmts ::= c_stmt (42)
        32     _stmts ::= stmts (42)
L. 69:  28-72  ifstmt ::= testexpr stmts \e__come_froms (42)
L. 69:  28-72  iflaststmt ::= testexpr stmts (42)
Reduce iflaststmt invalid by check
        32     stmts_opt ::= stmts (42)
        32     _stmts ::= stmts (42)
        32     stmts ::= sstmt (42)
L. 69:  28     _stmts ::= stmts (42)
L. 66:  24-72  ifstmt ::= testexpr stmts \e__come_froms (42)
Reduce ifstmt invalid by check
L. 66:  24-72  iflaststmt ::= testexpr stmts (42)
Reduce iflaststmt invalid by check
L. 69:  28     stmts_opt ::= stmts (42)
L. 69:  28     _stmts ::= stmts (42)
L. 69:  28     stmts ::= sstmt (42)
L. 69:  28-72  iflaststmtc ::= testexpr c_stmts (42)
Reduce iflaststmtc invalid by check
        32     c_stmts_opt ::= c_stmts (42)
        32     ifstmts_jumpc ::= c_stmts (42)
L. 69:  28-72  iflaststmtc ::= testexprc c_stmts (42)
Reduce iflaststmtc invalid by check
L. 69:  28     c_stmts_opt ::= c_stmts (42)
L. 66:  24-72  iflaststmtc ::= testexpr c_stmts (42)
Reduce iflaststmtc invalid by check
L. 69:  28     c_stmts_opt ::= c_stmts (42)
L. 69:  28     ifstmts_jumpc ::= c_stmts (42)
L. 66:  24-72  iflaststmtc ::= testexprc c_stmts (42)
Reduce iflaststmtc invalid by check
        32     c_stmts ::= _stmts (42)
        32     c_stmts ::= _stmts (42)
L. 69:  28     c_stmts ::= _stmts (42)
L. 69:  28     c_stmts ::= _stmts (42)
L. 76:  72     expr ::= LOAD_FAST (43)
L. 76:  72     return_expr ::= expr (43)
L. 76:  72     return_expr ::= expr (43)
        74     expr ::= LOAD_CONST (44)
        76     inplace_op ::= INPLACE_ADD (45)
        78     store ::= STORE_FAST (46)
L. 76:  72-78  aug_assign1 ::= expr expr inplace_op store (46)
L. 76:  72     stmt ::= aug_assign1 (46)
L. 76:  72     stmts ::= stmt (46)
L. 76:  72     c_stmt ::= stmt (46)
L. 76:  72     sstmt ::= stmt (46)
        32-78  stmts ::= stmts stmt (46)
L. 69:  28-78  stmts ::= stmts stmt (46)
L. 76:  72     _stmts ::= stmts (46)
L. 76:  72     c_stmts ::= c_stmt (46)
        32-78  c_stmts ::= c_stmts c_stmt (46)
L. 66:  24-78  c_stmts ::= c_stmts c_stmt (46)
L. 69:  28-78  c_stmts ::= c_stmts c_stmt (46)
L. 76:  72     stmts ::= sstmt (46)
        32-78  stmts ::= stmts sstmt (46)
L. 69:  28-78  stmts ::= stmts sstmt (46)
        32     _stmts ::= stmts (46)
L. 69:  28-78  ifstmt ::= testexpr stmts \e__come_froms (46)
Reduce ifstmt invalid by check
L. 69:  28-78  iflaststmt ::= testexpr stmts (46)
Reduce iflaststmt invalid by check
        32     stmts_opt ::= stmts (46)
        32     _stmts ::= stmts (46)
L. 69:  28     _stmts ::= stmts (46)
L. 66:  24-78  ifstmt ::= testexpr stmts \e__come_froms (46)
Reduce ifstmt invalid by check
L. 66:  24-78  iflaststmt ::= testexpr stmts (46)
Reduce iflaststmt invalid by check
L. 69:  28     stmts_opt ::= stmts (46)
L. 69:  28     _stmts ::= stmts (46)
L. 76:  72     c_stmts ::= _stmts (46)
L. 76:  72     suite_stmts ::= _stmts (46)
L. 76:  72     c_stmts ::= _stmts (46)
L. 69:  28-78  iflaststmtc ::= testexpr c_stmts (46)
Reduce iflaststmtc invalid by check
        32     c_stmts_opt ::= c_stmts (46)
        32     ifstmts_jumpc ::= c_stmts (46)
L. 69:  28-78  iflaststmtc ::= testexprc c_stmts (46)
Reduce iflaststmtc invalid by check
L. 69:  28     c_stmts_opt ::= c_stmts (46)
L. 66:  24-78  iflaststmtc ::= testexpr c_stmts (46)
Reduce iflaststmtc invalid by check
L. 69:  28     c_stmts_opt ::= c_stmts (46)
L. 69:  28     ifstmts_jumpc ::= c_stmts (46)
L. 66:  24-78  iflaststmtc ::= testexprc c_stmts (46)
Reduce iflaststmtc invalid by check
        32     c_stmts ::= _stmts (46)
        32     c_stmts ::= _stmts (46)
L. 69:  28     c_stmts ::= _stmts (46)
L. 69:  28     c_stmts ::= _stmts (46)
L. 76:  72     else_suite ::= suite_stmts (46)
L. 69:  28-78  ifstmtc ::= testexpr ifstmts_jumpc (46)
L. 69:  28-78  ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms (46)
Reduce ifstmtc invalid by check
L. 69:  28-78  if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms (46)
Reduce if_not_stmtc invalid by check
L. 66:  24-78  ifstmtc ::= testexpr ifstmts_jumpc (46)
Reduce ifstmtc invalid by check
L. 66:  24-78  ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms (46)
Reduce ifstmtc invalid by check
L. 66:  24-78  if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms (46)
        32-78  ifelsestmtc ::= testexpr c_stmts come_froms else_suite (46)
Reduce ifelsestmtc invalid by check
L. 66:  24-78  ifelsestmtc ::= testexpr c_stmts come_froms else_suite (46)
Reduce ifelsestmtc invalid by check
L. 69:  28-78  ifelsestmtc ::= testexpr c_stmts come_froms else_suite (46)
Reduce ifelsestmtc invalid by check
L. 69:  28     c_stmt ::= ifstmtc (46)
L. 66:  24     c_stmt ::= if_not_stmtc (46)
L. 69:  28     c_stmts ::= c_stmt (46)
L. 66:  24     c_stmts ::= c_stmt (46)
L. 78:  80     expr ::= LOAD_FAST (47)
L. 78:  80     return_expr ::= expr (47)
L. 78:  80     return_expr ::= expr (47)
L. 78:  80-82  attribute ::= expr LOAD_ATTR (48)
L. 78:  80     expr ::= attribute (48)
L. 78:  80     return_expr ::= expr (48)
L. 78:  80     return_expr ::= expr (48)
L. 78:  80-84  attribute37 ::= expr LOAD_METHOD (49)
L. 78:  80     expr ::= attribute37 (49)
L. 78:  80     return_expr ::= expr (49)
L. 78:  80     return_expr ::= expr (49)
        86     expr ::= LOAD_GLOBAL (50)
        88     expr ::= LOAD_STR (51)
        86-90  subscript ::= expr expr BINARY_SUBSCR (52)
        86     expr ::= subscript (52)
L. 78:  80-92  call ::= expr expr CALL_METHOD_1 (53)
L. 78:  80     expr ::= call (53)
L. 78:  80     return_expr ::= expr (53)
L. 78:  80     return_expr ::= expr (53)
L. 78:  80-94  expr_stmt ::= expr POP_TOP (54)
L. 78:  80     stmt ::= expr_stmt (54)
L. 76:  72-94  stmts ::= stmts stmt (54)
L. 78:  80     stmts ::= stmt (54)
L. 78:  80     c_stmt ::= stmt (54)
L. 78:  80     sstmt ::= stmt (54)
        32-94  stmts ::= stmts stmt (54)
L. 69:  28-94  stmts ::= stmts stmt (54)
L. 76:  72     _stmts ::= stmts (54)
L. 78:  80     _stmts ::= stmts (54)
L. 78:  80     c_stmts ::= c_stmt (54)
L. 76:  72-94  c_stmts ::= c_stmts c_stmt (54)
        32-94  c_stmts ::= c_stmts c_stmt (54)
L. 66:  24-94  c_stmts ::= c_stmts c_stmt (54)
L. 69:  28-94  c_stmts ::= c_stmts c_stmt (54)
L. 76:  72-94  stmts ::= stmts sstmt (54)
L. 78:  80     stmts ::= sstmt (54)
        32-94  stmts ::= stmts sstmt (54)
L. 69:  28-94  stmts ::= stmts sstmt (54)
        32     _stmts ::= stmts (54)
L. 69:  28-94  ifstmt ::= testexpr stmts \e__come_froms (54)
Reduce ifstmt invalid by check
L. 69:  28-94  iflaststmt ::= testexpr stmts (54)
Reduce iflaststmt invalid by check
        32     stmts_opt ::= stmts (54)
        32     _stmts ::= stmts (54)
L. 69:  28     _stmts ::= stmts (54)
L. 66:  24-94  ifstmt ::= testexpr stmts \e__come_froms (54)
Reduce ifstmt invalid by check
L. 66:  24-94  iflaststmt ::= testexpr stmts (54)
Reduce iflaststmt invalid by check
L. 69:  28     stmts_opt ::= stmts (54)
L. 69:  28     _stmts ::= stmts (54)
L. 76:  72     c_stmts ::= _stmts (54)
L. 76:  72     suite_stmts ::= _stmts (54)
L. 76:  72     c_stmts ::= _stmts (54)
L. 78:  80     c_stmts ::= _stmts (54)
L. 69:  28-94  iflaststmtc ::= testexpr c_stmts (54)
Reduce iflaststmtc invalid by check
        32     c_stmts_opt ::= c_stmts (54)
        32     ifstmts_jumpc ::= c_stmts (54)
L. 69:  28-94  iflaststmtc ::= testexprc c_stmts (54)
Reduce iflaststmtc invalid by check
L. 69:  28     c_stmts_opt ::= c_stmts (54)
L. 66:  24-94  iflaststmtc ::= testexpr c_stmts (54)
Reduce iflaststmtc invalid by check
L. 69:  28     c_stmts_opt ::= c_stmts (54)
L. 69:  28     ifstmts_jumpc ::= c_stmts (54)
L. 66:  24-94  iflaststmtc ::= testexprc c_stmts (54)
Reduce iflaststmtc invalid by check
        32     c_stmts ::= _stmts (54)
        32     c_stmts ::= _stmts (54)
L. 69:  28     c_stmts ::= _stmts (54)
L. 69:  28     c_stmts ::= _stmts (54)
L. 76:  72     else_suite ::= suite_stmts (54)
L. 69:  28-94  ifstmtc ::= testexpr ifstmts_jumpc (54)
L. 69:  28-94  ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms (54)
Reduce ifstmtc invalid by check
L. 69:  28-94  if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms (54)
Reduce if_not_stmtc invalid by check
L. 66:  24-94  ifstmtc ::= testexpr ifstmts_jumpc (54)
Reduce ifstmtc invalid by check
L. 66:  24-94  ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms (54)
Reduce ifstmtc invalid by check
L. 66:  24-94  if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms (54)
        32-94  ifelsestmtc ::= testexpr c_stmts come_froms else_suite (54)
Reduce ifelsestmtc invalid by check
L. 66:  24-94  ifelsestmtc ::= testexpr c_stmts come_froms else_suite (54)
Reduce ifelsestmtc invalid by check
L. 69:  28-94  ifelsestmtc ::= testexpr c_stmts come_froms else_suite (54)
Reduce ifelsestmtc invalid by check
L. 69:  28     c_stmt ::= ifstmtc (54)
L. 66:  24     c_stmt ::= if_not_stmtc (54)
L. 69:  28     c_stmts ::= c_stmt (54)
L. 66:  24     c_stmts ::= c_stmt (54)
L. 80:  96     expr ::= LOAD_FAST (55)
L. 80:  96     return_expr ::= expr (55)
L. 80:  96     return_expr ::= expr (55)
L. 80:  96-98  attribute ::= expr LOAD_ATTR (56)
L. 80:  96     expr ::= attribute (56)
L. 80:  96     return_expr ::= expr (56)
L. 80:  96     return_expr ::= expr (56)
L. 80:  96-100 attribute37 ::= expr LOAD_METHOD (57)
L. 80:  96     expr ::= attribute37 (57)
L. 80:  96     return_expr ::= expr (57)
L. 80:  96     return_expr ::= expr (57)
       102     expr ::= LOAD_FAST (58)
       102-104 attribute ::= expr LOAD_ATTR (59)
       102     expr ::= attribute (59)
       102-106 attribute37 ::= expr LOAD_METHOD (60)
       102     expr ::= attribute37 (60)
       102-108 call ::= expr CALL_METHOD_0 (61)
       102     expr ::= call (61)
       110     expr ::= LOAD_CONST (62)
       112     binary_operator ::= BINARY_ADD (63)
       102-112 bin_op ::= expr expr binary_operator (63)
       102     expr ::= bin_op (63)
L. 80:  96-114 call ::= expr expr CALL_METHOD_1 (64)
L. 80:  96     expr ::= call (64)
L. 80:  96     return_expr ::= expr (64)
L. 80:  96     return_expr ::= expr (64)
L. 80:  96-116 expr_stmt ::= expr POP_TOP (65)
L. 80:  96     stmt ::= expr_stmt (65)
L. 76:  72-116 stmts ::= stmts stmt (65)
L. 80:  96     stmts ::= stmt (65)
L. 80:  96     c_stmt ::= stmt (65)
L. 80:  96     sstmt ::= stmt (65)
L. 78:  80-116 stmts ::= stmts stmt (65)
        32-116 stmts ::= stmts stmt (65)
L. 69:  28-116 stmts ::= stmts stmt (65)
L. 76:  72     _stmts ::= stmts (65)
L. 80:  96     _stmts ::= stmts (65)
L. 80:  96     c_stmts ::= c_stmt (65)
L. 78:  80-116 c_stmts ::= c_stmts c_stmt (65)
L. 76:  72-116 c_stmts ::= c_stmts c_stmt (65)
        32-116 c_stmts ::= c_stmts c_stmt (65)
L. 66:  24-116 c_stmts ::= c_stmts c_stmt (65)
L. 69:  28-116 c_stmts ::= c_stmts c_stmt (65)
L. 76:  72-116 stmts ::= stmts sstmt (65)
L. 80:  96     stmts ::= sstmt (65)
L. 78:  80-116 stmts ::= stmts sstmt (65)
        32-116 stmts ::= stmts sstmt (65)
L. 69:  28-116 stmts ::= stmts sstmt (65)
L. 78:  80     _stmts ::= stmts (65)
        32     _stmts ::= stmts (65)
L. 69:  28-116 ifstmt ::= testexpr stmts \e__come_froms (65)
Reduce ifstmt invalid by check
L. 69:  28-116 iflaststmt ::= testexpr stmts (65)
Reduce iflaststmt invalid by check
        32     stmts_opt ::= stmts (65)
        32     _stmts ::= stmts (65)
L. 69:  28     _stmts ::= stmts (65)
L. 66:  24-116 ifstmt ::= testexpr stmts \e__come_froms (65)
Reduce ifstmt invalid by check
L. 66:  24-116 iflaststmt ::= testexpr stmts (65)
Reduce iflaststmt invalid by check
L. 69:  28     stmts_opt ::= stmts (65)
L. 69:  28     _stmts ::= stmts (65)
L. 76:  72     c_stmts ::= _stmts (65)
L. 76:  72     suite_stmts ::= _stmts (65)
L. 76:  72     c_stmts ::= _stmts (65)
L. 80:  96     c_stmts ::= _stmts (65)
L. 69:  28-116 iflaststmtc ::= testexpr c_stmts (65)
Reduce iflaststmtc invalid by check
        32     c_stmts_opt ::= c_stmts (65)
        32     ifstmts_jumpc ::= c_stmts (65)
L. 69:  28-116 iflaststmtc ::= testexprc c_stmts (65)
Reduce iflaststmtc invalid by check
L. 69:  28     c_stmts_opt ::= c_stmts (65)
L. 66:  24-116 iflaststmtc ::= testexpr c_stmts (65)
Reduce iflaststmtc invalid by check
L. 69:  28     c_stmts_opt ::= c_stmts (65)
L. 69:  28     ifstmts_jumpc ::= c_stmts (65)
L. 66:  24-116 iflaststmtc ::= testexprc c_stmts (65)
Reduce iflaststmtc invalid by check
L. 78:  80     c_stmts ::= _stmts (65)
        32     c_stmts ::= _stmts (65)
        32     c_stmts ::= _stmts (65)
L. 69:  28     c_stmts ::= _stmts (65)
L. 69:  28     c_stmts ::= _stmts (65)
L. 76:  72     else_suite ::= suite_stmts (65)
L. 69:  28-116 ifstmtc ::= testexpr ifstmts_jumpc (65)
L. 69:  28-116 ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms (65)
Reduce ifstmtc invalid by check
L. 69:  28-116 if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms (65)
Reduce if_not_stmtc invalid by check
L. 66:  24-116 ifstmtc ::= testexpr ifstmts_jumpc (65)
Reduce ifstmtc invalid by check
L. 66:  24-116 ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms (65)
Reduce ifstmtc invalid by check
L. 66:  24-116 if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms (65)
        32-116 ifelsestmtc ::= testexpr c_stmts come_froms else_suite (65)
Reduce ifelsestmtc invalid by check
L. 66:  24-116 ifelsestmtc ::= testexpr c_stmts come_froms else_suite (65)
Reduce ifelsestmtc invalid by check
L. 69:  28-116 ifelsestmtc ::= testexpr c_stmts come_froms else_suite (65)
Reduce ifelsestmtc invalid by check
L. 69:  28     c_stmt ::= ifstmtc (65)
L. 66:  24     c_stmt ::= if_not_stmtc (65)
L. 69:  28     c_stmts ::= c_stmt (65)
L. 66:  24     c_stmts ::= c_stmt (65)
L. 83: 118     expr ::= LOAD_FAST (66)
L. 83: 118     return_expr ::= expr (66)
L. 83: 118     return_expr ::= expr (66)
L. 83: 118-120 attribute ::= expr LOAD_ATTR (67)
L. 83: 118     expr ::= attribute (67)
L. 83: 118     return_expr ::= expr (67)
L. 83: 118     return_expr ::= expr (67)
L. 83: 118-122 attribute37 ::= expr LOAD_METHOD (68)
L. 83: 118     expr ::= attribute37 (68)
L. 83: 118     return_expr ::= expr (68)
L. 83: 118     return_expr ::= expr (68)
       124     list ::= BUILD_LIST_0 (69)
       124     expr ::= list (69)
       126     expr ::= LOAD_CONST (70)
       126     expr_or_arg ::= expr (70)
L. 83: 118-128 call ::= expr expr expr CALL_METHOD_2 (71)
L. 83: 118     expr ::= call (71)
L. 83: 118     return_expr ::= expr (71)
L. 83: 118     return_expr ::= expr (71)
       130     store ::= STORE_FAST (72)
L. 83: 118-130 assign ::= expr store (72)
L. 83: 118     stmt ::= assign (72)
L. 76:  72-130 stmts ::= stmts stmt (72)
L. 83: 118     stmts ::= stmt (72)
L. 83: 118     c_stmt ::= stmt (72)
L. 83: 118     sstmt ::= stmt (72)
L. 80:  96-130 stmts ::= stmts stmt (72)
L. 78:  80-130 stmts ::= stmts stmt (72)
        32-130 stmts ::= stmts stmt (72)
L. 69:  28-130 stmts ::= stmts stmt (72)
L. 76:  72     _stmts ::= stmts (72)
L. 83: 118     _stmts ::= stmts (72)
L. 83: 118     c_stmts ::= c_stmt (72)
L. 80:  96-130 c_stmts ::= c_stmts c_stmt (72)
L. 78:  80-130 c_stmts ::= c_stmts c_stmt (72)
L. 76:  72-130 c_stmts ::= c_stmts c_stmt (72)
        32-130 c_stmts ::= c_stmts c_stmt (72)
L. 66:  24-130 c_stmts ::= c_stmts c_stmt (72)
L. 69:  28-130 c_stmts ::= c_stmts c_stmt (72)
L. 76:  72-130 stmts ::= stmts sstmt (72)
L. 83: 118     stmts ::= sstmt (72)
L. 80:  96-130 stmts ::= stmts sstmt (72)
L. 78:  80-130 stmts ::= stmts sstmt (72)
        32-130 stmts ::= stmts sstmt (72)
L. 69:  28-130 stmts ::= stmts sstmt (72)
L. 80:  96     _stmts ::= stmts (72)
L. 78:  80     _stmts ::= stmts (72)
        32     _stmts ::= stmts (72)
L. 69:  28-130 ifstmt ::= testexpr stmts \e__come_froms (72)
Reduce ifstmt invalid by check
L. 69:  28-130 iflaststmt ::= testexpr stmts (72)
Reduce iflaststmt invalid by check
        32     stmts_opt ::= stmts (72)
        32     _stmts ::= stmts (72)
L. 69:  28     _stmts ::= stmts (72)
L. 66:  24-130 ifstmt ::= testexpr stmts \e__come_froms (72)
Reduce ifstmt invalid by check
L. 66:  24-130 iflaststmt ::= testexpr stmts (72)
Reduce iflaststmt invalid by check
L. 69:  28     stmts_opt ::= stmts (72)
L. 69:  28     _stmts ::= stmts (72)
L. 76:  72     c_stmts ::= _stmts (72)
L. 76:  72     suite_stmts ::= _stmts (72)
L. 76:  72     c_stmts ::= _stmts (72)
L. 83: 118     c_stmts ::= _stmts (72)
L. 69:  28-130 iflaststmtc ::= testexpr c_stmts (72)
Reduce iflaststmtc invalid by check
        32     c_stmts_opt ::= c_stmts (72)
        32     ifstmts_jumpc ::= c_stmts (72)
L. 69:  28-130 iflaststmtc ::= testexprc c_stmts (72)
Reduce iflaststmtc invalid by check
L. 69:  28     c_stmts_opt ::= c_stmts (72)
L. 66:  24-130 iflaststmtc ::= testexpr c_stmts (72)
Reduce iflaststmtc invalid by check
L. 69:  28     c_stmts_opt ::= c_stmts (72)
L. 69:  28     ifstmts_jumpc ::= c_stmts (72)
L. 66:  24-130 iflaststmtc ::= testexprc c_stmts (72)
Reduce iflaststmtc invalid by check
L. 80:  96     c_stmts ::= _stmts (72)
L. 78:  80     c_stmts ::= _stmts (72)
        32     c_stmts ::= _stmts (72)
        32     c_stmts ::= _stmts (72)
L. 69:  28     c_stmts ::= _stmts (72)
L. 69:  28     c_stmts ::= _stmts (72)
L. 76:  72     else_suite ::= suite_stmts (72)
L. 69:  28-130 ifstmtc ::= testexpr ifstmts_jumpc (72)
L. 69:  28-130 ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms (72)
Reduce ifstmtc invalid by check
L. 69:  28-130 if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms (72)
Reduce if_not_stmtc invalid by check
L. 66:  24-130 ifstmtc ::= testexpr ifstmts_jumpc (72)
Reduce ifstmtc invalid by check
L. 66:  24-130 ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms (72)
Reduce ifstmtc invalid by check
L. 66:  24-130 if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms (72)
        32-130 ifelsestmtc ::= testexpr c_stmts come_froms else_suite (72)
Reduce ifelsestmtc invalid by check
L. 66:  24-130 ifelsestmtc ::= testexpr c_stmts come_froms else_suite (72)
Reduce ifelsestmtc invalid by check
L. 69:  28-130 ifelsestmtc ::= testexpr c_stmts come_froms else_suite (72)
Reduce ifelsestmtc invalid by check
L. 69:  28     c_stmt ::= ifstmtc (72)
L. 66:  24     c_stmt ::= if_not_stmtc (72)
L. 69:  28     c_stmts ::= c_stmt (72)
L. 66:  24     c_stmts ::= c_stmt (72)
L. 84: 132     expr ::= LOAD_FAST (73)
L. 84: 132     return_expr ::= expr (73)
L. 84: 132     return_expr ::= expr (73)
       134     expr ::= LOAD_CONST (74)
L. 84: 132-136 compare_single ::= expr expr COMPARE_OP (75)
L. 84: 132     compare ::= compare_single (75)
L. 84: 132     expr ::= compare (75)
L. 84: 132     return_expr ::= expr (75)
L. 84: 132     return_expr ::= expr (75)
L. 84: 132-138 expr_pjif ::= expr POP_JUMP_IF_FALSE (76)
L. 84: 132-138 expr_pjif ::= expr POP_JUMP_IF_FALSE (76)
L. 84: 132     testfalse ::= expr_pjif (76)
L. 84: 132     and_parts ::= expr_pjif (76)
L. 84: 132     and_parts ::= expr_pjif (76)
L. 84: 132     testfalse ::= expr_pjif (76)
L. 84: 132     testexpr ::= testfalse (76)
L. 84: 132     testexprc ::= testexpr (76)
L. 84: 132     testexprc ::= testexpr (76)
L. 85: 140     expr ::= LOAD_GLOBAL (77)
L. 85: 140     return_expr ::= expr (77)
L. 85: 140-142 attribute37 ::= expr LOAD_METHOD (78)
L. 85: 140     expr ::= attribute37 (78)
L. 85: 140     return_expr ::= expr (78)
       144     expr ::= LOAD_STR (79)
L. 85: 140-146 call ::= expr expr CALL_METHOD_1 (80)
L. 85: 140     expr ::= call (80)
L. 85: 140     return_expr ::= expr (80)
L. 85: 140-148 expr_stmt ::= expr POP_TOP (81)
L. 85: 140     stmt ::= expr_stmt (81)
L. 85: 140     stmts ::= stmt (81)
L. 85: 140     c_stmt ::= stmt (81)
L. 85: 140     sstmt ::= stmt (81)
L. 84: 132-148 ifstmt ::= testexpr stmts \e__come_froms (81)
L. 84: 132-148 iflaststmt ::= testexpr stmts (81)
Reduce iflaststmt invalid by check
L. 85: 140     stmts_opt ::= stmts (81)
L. 85: 140     _stmts ::= stmts (81)
L. 85: 140     _stmts ::= stmts (81)
L. 85: 140     c_stmts ::= c_stmt (81)
L. 85: 140     stmts ::= sstmt (81)
L. 84: 132     stmt ::= ifstmt (81)
L. 85: 140     c_stmts ::= _stmts (81)
L. 85: 140     c_stmts ::= _stmts (81)
L. 84: 132-148 iflaststmtc ::= testexpr c_stmts (81)
Reduce iflaststmtc invalid by check
L. 85: 140     c_stmts_opt ::= c_stmts (81)
L. 85: 140     ifstmts_jumpc ::= c_stmts (81)
L. 84: 132-148 iflaststmtc ::= testexpr c_stmts (81)
Reduce iflaststmtc invalid by check
L. 85: 140     c_stmts_opt ::= c_stmts (81)
L. 84: 132-148 iflaststmtc ::= testexprc c_stmts (81)
Reduce iflaststmtc invalid by check
L. 76:  72-148 stmts ::= stmts stmt (81)
L. 84: 132     stmts ::= stmt (81)
L. 84: 132     c_stmt ::= stmt (81)
L. 84: 132     sstmt ::= stmt (81)
L. 83: 118-148 stmts ::= stmts stmt (81)
L. 80:  96-148 stmts ::= stmts stmt (81)
L. 78:  80-148 stmts ::= stmts stmt (81)
        32-148 stmts ::= stmts stmt (81)
L. 69:  28-148 stmts ::= stmts stmt (81)
L. 84: 132-148 ifstmtc ::= testexpr ifstmts_jumpc (81)
L. 84: 132-148 ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms (81)
L. 84: 132-148 if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms (81)
L. 76:  72     _stmts ::= stmts (81)
L. 84: 132     _stmts ::= stmts (81)
L. 84: 132     c_stmts ::= c_stmt (81)
L. 83: 118-148 c_stmts ::= c_stmts c_stmt (81)
L. 80:  96-148 c_stmts ::= c_stmts c_stmt (81)
L. 78:  80-148 c_stmts ::= c_stmts c_stmt (81)
L. 76:  72-148 c_stmts ::= c_stmts c_stmt (81)
        32-148 c_stmts ::= c_stmts c_stmt (81)
L. 66:  24-148 c_stmts ::= c_stmts c_stmt (81)
L. 69:  28-148 c_stmts ::= c_stmts c_stmt (81)
L. 76:  72-148 stmts ::= stmts sstmt (81)
L. 84: 132     stmts ::= sstmt (81)
L. 83: 118-148 stmts ::= stmts sstmt (81)
L. 80:  96-148 stmts ::= stmts sstmt (81)
L. 78:  80-148 stmts ::= stmts sstmt (81)
        32-148 stmts ::= stmts sstmt (81)
L. 69:  28-148 stmts ::= stmts sstmt (81)
L. 83: 118     _stmts ::= stmts (81)
L. 80:  96     _stmts ::= stmts (81)
L. 78:  80     _stmts ::= stmts (81)
        32     _stmts ::= stmts (81)
L. 69:  28-148 ifstmt ::= testexpr stmts \e__come_froms (81)
Reduce ifstmt invalid by check
L. 69:  28-148 iflaststmt ::= testexpr stmts (81)
Reduce iflaststmt invalid by check
        32     stmts_opt ::= stmts (81)
        32     _stmts ::= stmts (81)
L. 69:  28     _stmts ::= stmts (81)
L. 66:  24-148 ifstmt ::= testexpr stmts \e__come_froms (81)
L. 66:  24-148 iflaststmt ::= testexpr stmts (81)
Reduce iflaststmt invalid by check
L. 69:  28     stmts_opt ::= stmts (81)
L. 69:  28     _stmts ::= stmts (81)
L. 84: 132     c_stmt ::= ifstmtc (81)
L. 84: 132     c_stmt ::= if_not_stmtc (81)
L. 76:  72     c_stmts ::= _stmts (81)
L. 76:  72     suite_stmts ::= _stmts (81)
L. 76:  72     c_stmts ::= _stmts (81)
L. 84: 132     c_stmts ::= _stmts (81)
L. 69:  28-148 iflaststmtc ::= testexpr c_stmts (81)
Reduce iflaststmtc invalid by check
        32     c_stmts_opt ::= c_stmts (81)
        32     ifstmts_jumpc ::= c_stmts (81)
L. 69:  28-148 iflaststmtc ::= testexprc c_stmts (81)
Reduce iflaststmtc invalid by check
L. 69:  28     c_stmts_opt ::= c_stmts (81)
L. 66:  24-148 iflaststmtc ::= testexpr c_stmts (81)
Reduce iflaststmtc invalid by check
L. 69:  28     c_stmts_opt ::= c_stmts (81)
L. 69:  28     ifstmts_jumpc ::= c_stmts (81)
L. 66:  24-148 iflaststmtc ::= testexprc c_stmts (81)
Reduce iflaststmtc invalid by check
L. 83: 118     c_stmts ::= _stmts (81)
L. 80:  96     c_stmts ::= _stmts (81)
L. 78:  80     c_stmts ::= _stmts (81)
        32     c_stmts ::= _stmts (81)
        32     c_stmts ::= _stmts (81)
L. 69:  28     c_stmts ::= _stmts (81)
L. 69:  28     c_stmts ::= _stmts (81)
L. 66:  24     stmt ::= ifstmt (81)
L. 76:  72     else_suite ::= suite_stmts (81)
L. 69:  28-148 ifstmtc ::= testexpr ifstmts_jumpc (81)
Reduce ifstmtc invalid by check
L. 69:  28-148 ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms (81)
Reduce ifstmtc invalid by check
L. 69:  28-148 if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms (81)
Reduce if_not_stmtc invalid by check
L. 66:  24-148 ifstmtc ::= testexpr ifstmts_jumpc (81)
L. 66:  24-148 ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms (81)
L. 66:  24-148 if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms (81)
L. 66:  24     stmts ::= stmt (81)
L. 66:  24     c_stmt ::= stmt (81)
L. 66:  24     sstmt ::= stmt (81)
        32-148 ifelsestmtc ::= testexpr c_stmts come_froms else_suite (81)
Reduce ifelsestmtc invalid by check
L. 66:  24-148 ifelsestmtc ::= testexpr c_stmts come_froms else_suite (81)
Reduce ifelsestmtc invalid by check
L. 69:  28-148 ifelsestmtc ::= testexpr c_stmts come_froms else_suite (81)
Reduce ifelsestmtc invalid by check
L. 66:  24     c_stmt ::= ifstmtc (81)
L. 66:  24     c_stmt ::= if_not_stmtc (81)
L. 66:  24     _stmts ::= stmts (81)
L. 66:  24     c_stmts ::= c_stmt (81)
L. 66:  24     stmts ::= sstmt (81)
L. 66:  24     c_stmts ::= _stmts (81)
L. 87: 150-150 whileTruestmt38 ::= \e__come_froms \e_pass JUMP_LOOP (82)
Reduce whileTruestmt38 invalid by check
L. 84: 132-150 whilestmt38 ::= \e__come_froms testexpr c_stmts JUMP_LOOP \e__come_froms (82)
Reduce whilestmt38 invalid by check
L. 84: 132-150 iflaststmtc ::= testexpr c_stmts JUMP_LOOP (82)
Reduce iflaststmtc invalid by check
L. 85: 140-150 ifstmts_jumpc ::= c_stmts JUMP_LOOP (82)
L. 85: 140-150 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP \e__come_froms (82)
Reduce whileTruestmt38 invalid by check
L. 84: 132-150 iflaststmtc ::= testexpr c_stmts JUMP_LOOP (82)
Reduce iflaststmtc invalid by check
L. 85: 140-150 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP \e__come_froms (82)
Reduce whileTruestmt38 invalid by check
L. 84: 132-150 iflaststmtc ::= testexprc c_stmts JUMP_LOOP \e_opt_pop_block (82)
Reduce iflaststmtc invalid by check
L. 84: 132-150 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP \e__come_froms (82)
Reduce whileTruestmt38 invalid by check
L. 83: 118-150 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP \e__come_froms (82)
Reduce whileTruestmt38 invalid by check
L. 80:  96-150 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP \e__come_froms (82)
Reduce whileTruestmt38 invalid by check
L. 78:  80-150 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP \e__come_froms (82)
Reduce whileTruestmt38 invalid by check
        72-150 whileTruestmt38 ::= _come_froms c_stmts JUMP_LOOP \e__come_froms (82)
Reduce whileTruestmt38 invalid by check
L. 76:  72-150 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP \e__come_froms (82)
Reduce whileTruestmt38 invalid by check
        72-150 whileTruestmt38 ::= _come_froms c_stmts JUMP_LOOP \e__come_froms (82)
Reduce whileTruestmt38 invalid by check
        32-150 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP \e__come_froms (82)
Reduce whileTruestmt38 invalid by check
L. 69:  28-150 whilestmt38 ::= \e__come_froms testexpr c_stmts JUMP_LOOP \e__come_froms (82)
Reduce whilestmt38 invalid by check
L. 69:  28-150 iflaststmtc ::= testexpr c_stmts JUMP_LOOP (82)
Reduce iflaststmtc invalid by check
        32-150 ifstmts_jumpc ::= c_stmts JUMP_LOOP (82)
        32-150 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP \e__come_froms (82)
Reduce whileTruestmt38 invalid by check
L. 69:  28-150 iflaststmtc ::= testexprc c_stmts JUMP_LOOP \e_opt_pop_block (82)
Reduce iflaststmtc invalid by check
        24-150 whileTruestmt38 ::= _come_froms c_stmts JUMP_LOOP \e__come_froms (82)
Reduce whileTruestmt38 invalid by check
L. 66:  24-150 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP \e__come_froms (82)
Reduce whileTruestmt38 invalid by check
        24-150 whileTruestmt38 ::= _come_froms c_stmts JUMP_LOOP \e__come_froms (82)
Reduce whileTruestmt38 invalid by check
        24-150 whileTruestmt38 ::= _come_froms c_stmts JUMP_LOOP \e__come_froms (82)
Reduce whileTruestmt38 invalid by check
        24-150 whilestmt38 ::= _come_froms testexpr c_stmts JUMP_LOOP \e__come_froms (82)
L. 69:  28-150 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP \e__come_froms (82)
Reduce whileTruestmt38 invalid by check
L. 66:  24-150 whilestmt38 ::= \e__come_froms testexpr c_stmts JUMP_LOOP \e__come_froms (82)
L. 66:  24-150 iflaststmtc ::= testexpr c_stmts JUMP_LOOP (82)
Reduce iflaststmtc invalid by check
L. 69:  28-150 ifstmts_jumpc ::= c_stmts JUMP_LOOP (82)
L. 69:  28-150 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP \e__come_froms (82)
Reduce whileTruestmt38 invalid by check
        24-150 whilestmt38 ::= _come_froms testexpr c_stmts JUMP_LOOP \e__come_froms (82)
        24-150 whilestmt38 ::= _come_froms testexpr c_stmts JUMP_LOOP \e__come_froms (82)
L. 66:  24-150 iflaststmtc ::= testexprc c_stmts JUMP_LOOP \e_opt_pop_block (82)
Reduce iflaststmtc invalid by check
L. 84: 132-150 ifstmtc ::= testexpr ifstmts_jumpc (82)
L. 84: 132-150 ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms (82)
L. 84: 132-150 if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms (82)
Reduce if_not_stmtc invalid by check
L. 69:  28-150 ifstmtc ::= testexpr ifstmts_jumpc (82)
L. 69:  28-150 ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms (82)
Reduce ifstmtc invalid by check
L. 69:  28-150 if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms (82)
Reduce if_not_stmtc invalid by check
        24     stmt ::= whilestmt38 (82)
L. 66:  24     stmt ::= whilestmt38 (82)
L. 66:  24-150 ifstmtc ::= testexpr ifstmts_jumpc (82)
Reduce ifstmtc invalid by check
L. 66:  24-150 ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms (82)
Reduce ifstmtc invalid by check
L. 66:  24-150 if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms (82)
        24     stmt ::= whilestmt38 (82)
        24     stmt ::= whilestmt38 (82)
L. 84: 132     c_stmt ::= ifstmtc (82)
L. 69:  28     c_stmt ::= ifstmtc (82)
        24     stmts ::= stmt (82)
        24     c_stmt ::= stmt (82)
        24     sstmt ::= stmt (82)
L. 66:  24     stmts ::= stmt (82)
L. 66:  24     c_stmt ::= stmt (82)
L. 66:  24     sstmt ::= stmt (82)
L. 66:  24     c_stmt ::= if_not_stmtc (82)
        24     stmts ::= stmt (82)
        24     c_stmt ::= stmt (82)
        24     sstmt ::= stmt (82)
        24     stmts ::= stmt (82)
        24     c_stmt ::= stmt (82)
        24     sstmt ::= stmt (82)
L. 84: 132     c_stmts ::= c_stmt (82)
L. 83: 118-150 c_stmts ::= c_stmts c_stmt (82)
L. 80:  96-150 c_stmts ::= c_stmts c_stmt (82)
L. 78:  80-150 c_stmts ::= c_stmts c_stmt (82)
L. 76:  72-150 c_stmts ::= c_stmts c_stmt (82)
        32-150 c_stmts ::= c_stmts c_stmt (82)
L. 66:  24-150 c_stmts ::= c_stmts c_stmt (82)
L. 69:  28-150 c_stmts ::= c_stmts c_stmt (82)
L. 69:  28     c_stmts ::= c_stmt (82)
        24     _stmts ::= stmts (82)
        24     c_stmts ::= c_stmt (82)
        24     stmts ::= sstmt (82)
L. 66:  24     _stmts ::= stmts (82)
L. 66:  24     c_stmts ::= c_stmt (82)
L. 66:  24     stmts ::= sstmt (82)
        24     _stmts ::= stmts (82)
        24     c_stmts ::= c_stmt (82)
        24     stmts ::= sstmt (82)
        24     _stmts ::= stmts (82)
        24     c_stmts ::= c_stmt (82)
        24     stmts ::= sstmt (82)
L. 69:  28-150 iflaststmtc ::= testexpr c_stmts (82)
Reduce iflaststmtc invalid by check
        32     c_stmts_opt ::= c_stmts (82)
        32     ifstmts_jumpc ::= c_stmts (82)
L. 69:  28-150 iflaststmtc ::= testexprc c_stmts (82)
Reduce iflaststmtc invalid by check
L. 69:  28     c_stmts_opt ::= c_stmts (82)
L. 66:  24-150 iflaststmtc ::= testexpr c_stmts (82)
Reduce iflaststmtc invalid by check
L. 69:  28     c_stmts_opt ::= c_stmts (82)
L. 69:  28     ifstmts_jumpc ::= c_stmts (82)
L. 66:  24-150 iflaststmtc ::= testexprc c_stmts (82)
Reduce iflaststmtc invalid by check
        24     suite_stmts ::= _stmts (82)
        24     c_stmts ::= _stmts (82)
        24     c_suite_stmts ::= c_stmts (82)
L. 66:  24     c_stmts ::= _stmts (82)
        24     c_stmts ::= _stmts (82)
        24     c_stmts ::= _stmts (82)
        24     suite_stmts_opt ::= suite_stmts (82)
        24     c_suite_stmts ::= suite_stmts (82)
        24     c_suite_stmts_opt ::= c_suite_stmts (82)
        24     c_suite_stmts_opt ::= suite_stmts_opt (82)
       152-152 _come_froms ::= \e__come_froms COME_FROM (83)
       152     come_froms ::= COME_FROM (83)
       152-152 _come_froms ::= \e__come_froms COME_FROM (83)
       152     come_froms ::= COME_FROM (83)
       152     come_from_opt ::= COME_FROM (83)
       152     come_froms ::= COME_FROM (83)
       152     come_from_opt ::= COME_FROM (83)
       152     come_froms ::= COME_FROM (83)
L. 84: 132-152 whilestmt38 ::= \e__come_froms testexpr c_stmts JUMP_LOOP _come_froms (83)
Reduce whilestmt38 invalid by check
L. 85: 140-152 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP _come_froms (83)
Reduce whileTruestmt38 invalid by check
L. 84: 132-152 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP _come_froms (83)
Reduce whileTruestmt38 invalid by check
L. 83: 118-152 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP _come_froms (83)
Reduce whileTruestmt38 invalid by check
L. 80:  96-152 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP _come_froms (83)
Reduce whileTruestmt38 invalid by check
L. 78:  80-152 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP _come_froms (83)
Reduce whileTruestmt38 invalid by check
        72-152 whileTruestmt38 ::= _come_froms c_stmts JUMP_LOOP _come_froms (83)
Reduce whileTruestmt38 invalid by check
L. 76:  72-152 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP _come_froms (83)
Reduce whileTruestmt38 invalid by check
        72-152 whileTruestmt38 ::= _come_froms c_stmts JUMP_LOOP _come_froms (83)
Reduce whileTruestmt38 invalid by check
        32-152 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP _come_froms (83)
Reduce whileTruestmt38 invalid by check
L. 69:  28-152 whilestmt38 ::= \e__come_froms testexpr c_stmts JUMP_LOOP _come_froms (83)
Reduce whilestmt38 invalid by check
        24-152 whileTruestmt38 ::= _come_froms c_stmts JUMP_LOOP _come_froms (83)
Reduce whileTruestmt38 invalid by check
L. 66:  24-152 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP _come_froms (83)
Reduce whileTruestmt38 invalid by check
        24-152 whileTruestmt38 ::= _come_froms c_stmts JUMP_LOOP _come_froms (83)
Reduce whileTruestmt38 invalid by check
        24-152 whileTruestmt38 ::= _come_froms c_stmts JUMP_LOOP _come_froms (83)
Reduce whileTruestmt38 invalid by check
        24-152 whilestmt38 ::= _come_froms testexpr c_stmts JUMP_LOOP _come_froms (83)
L. 69:  28-152 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP _come_froms (83)
Reduce whileTruestmt38 invalid by check
L. 66:  24-152 whilestmt38 ::= \e__come_froms testexpr c_stmts JUMP_LOOP _come_froms (83)
        24-152 whilestmt38 ::= _come_froms testexpr c_stmts JUMP_LOOP _come_froms (83)
        24-152 whilestmt38 ::= _come_froms testexpr c_stmts JUMP_LOOP _come_froms (83)
L. 84: 132-152 ifstmtc ::= testexprc ifstmts_jumpc _come_froms (83)
L. 84: 132-152 if_not_stmtc ::= testexprc ifstmts_jumpc _come_froms (83)
Reduce if_not_stmtc invalid by check
L. 69:  28-152 ifstmtc ::= testexprc ifstmts_jumpc _come_froms (83)
L. 69:  28-152 if_not_stmtc ::= testexprc ifstmts_jumpc _come_froms (83)
Reduce if_not_stmtc invalid by check
L. 66:  24-152 ifstmtc ::= testexprc ifstmts_jumpc _come_froms (83)
Reduce ifstmtc invalid by check
L. 66:  24-152 if_not_stmtc ::= testexprc ifstmts_jumpc _come_froms (83)
L. 84: 132-152 whilestmt38 ::= \e__come_froms testexpr c_stmts_opt JUMP_LOOP come_froms (83)
Reduce whilestmt38 invalid by check
L. 87: 150-152 jb_cfs ::= \e_come_from_opt JUMP_LOOP come_froms (83)
L. 69:  28-152 whilestmt38 ::= \e__come_froms testexpr c_stmts_opt JUMP_LOOP come_froms (83)
Reduce whilestmt38 invalid by check
        24-152 whilestmt38 ::= _come_froms testexpr c_stmts_opt JUMP_LOOP come_froms (83)
L. 66:  24-152 whilestmt38 ::= \e__come_froms testexpr c_stmts_opt JUMP_LOOP come_froms (83)
        24-152 whilestmt38 ::= _come_froms testexpr c_stmts_opt JUMP_LOOP come_froms (83)
        24-152 whilestmt38 ::= _come_froms testexpr c_stmts_opt JUMP_LOOP come_froms (83)
L. 69:  28-152 whilestmt38 ::= \e__come_froms testexpr c_stmts come_froms (83)
Reduce whilestmt38 invalid by check
L. 69:  28-152 iflaststmtc ::= testexpr c_stmts come_froms (83)
Reduce iflaststmtc invalid by check
        24-152 whilestmt38 ::= _come_froms testexpr c_stmts come_froms (83)
L. 66:  24-152 whilestmt38 ::= \e__come_froms testexpr c_stmts come_froms (83)
L. 66:  24-152 iflaststmtc ::= testexpr c_stmts come_froms (83)
Reduce iflaststmtc invalid by check
        24-152 whilestmt38 ::= _come_froms testexpr c_stmts come_froms (83)
        24-152 whilestmt38 ::= _come_froms testexpr c_stmts come_froms (83)
        32-152 ifstmts_jumpc ::= c_stmts_opt come_froms (83)
L. 69:  28-152 ifstmts_jumpc ::= c_stmts_opt come_froms (83)
        24     stmt ::= whilestmt38 (83)
L. 66:  24     stmt ::= whilestmt38 (83)
        24     stmt ::= whilestmt38 (83)
        24     stmt ::= whilestmt38 (83)
L. 84: 132     c_stmt ::= ifstmtc (83)
L. 69:  28     c_stmt ::= ifstmtc (83)
L. 66:  24     c_stmt ::= if_not_stmtc (83)
L. 69:  28-152 ifstmtc ::= testexpr ifstmts_jumpc (83)
L. 69:  28-152 ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms (83)
Reduce ifstmtc invalid by check
L. 69:  28-152 if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms (83)
Reduce if_not_stmtc invalid by check
L. 66:  24-152 ifstmtc ::= testexpr ifstmts_jumpc (83)
Reduce ifstmtc invalid by check
L. 66:  24-152 ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms (83)
Reduce ifstmtc invalid by check
L. 66:  24-152 if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms (83)
        24     stmts ::= stmt (83)
        24     c_stmt ::= stmt (83)
        24     sstmt ::= stmt (83)
L. 66:  24     stmts ::= stmt (83)
L. 66:  24     c_stmt ::= stmt (83)
L. 66:  24     sstmt ::= stmt (83)
        24     stmts ::= stmt (83)
        24     c_stmt ::= stmt (83)
        24     sstmt ::= stmt (83)
        24     stmts ::= stmt (83)
        24     c_stmt ::= stmt (83)
        24     sstmt ::= stmt (83)
L. 84: 132     c_stmts ::= c_stmt (83)
L. 83: 118-152 c_stmts ::= c_stmts c_stmt (83)
L. 80:  96-152 c_stmts ::= c_stmts c_stmt (83)
L. 78:  80-152 c_stmts ::= c_stmts c_stmt (83)
L. 76:  72-152 c_stmts ::= c_stmts c_stmt (83)
        32-152 c_stmts ::= c_stmts c_stmt (83)
L. 66:  24-152 c_stmts ::= c_stmts c_stmt (83)
L. 69:  28-152 c_stmts ::= c_stmts c_stmt (83)
L. 69:  28     c_stmts ::= c_stmt (83)
L. 66:  24     c_stmts ::= c_stmt (83)
        24     _stmts ::= stmts (83)
        24     c_stmts ::= c_stmt (83)
        24     stmts ::= sstmt (83)
L. 66:  24     _stmts ::= stmts (83)
L. 66:  24     stmts ::= sstmt (83)
        24     _stmts ::= stmts (83)
        24     c_stmts ::= c_stmt (83)
        24     stmts ::= sstmt (83)
        24     _stmts ::= stmts (83)
        24     c_stmts ::= c_stmt (83)
        24     stmts ::= sstmt (83)
L. 69:  28-152 iflaststmtc ::= testexpr c_stmts (83)
Reduce iflaststmtc invalid by check
        32     c_stmts_opt ::= c_stmts (83)
        32     ifstmts_jumpc ::= c_stmts (83)
L. 69:  28-152 iflaststmtc ::= testexprc c_stmts (83)
Reduce iflaststmtc invalid by check
L. 69:  28     c_stmts_opt ::= c_stmts (83)
L. 66:  24-152 iflaststmtc ::= testexpr c_stmts (83)
Reduce iflaststmtc invalid by check
L. 69:  28     c_stmts_opt ::= c_stmts (83)
L. 69:  28     ifstmts_jumpc ::= c_stmts (83)
L. 66:  24-152 iflaststmtc ::= testexprc c_stmts (83)
Reduce iflaststmtc invalid by check
        24     suite_stmts ::= _stmts (83)
        24     c_stmts ::= _stmts (83)
        24     c_suite_stmts ::= c_stmts (83)
L. 66:  24     c_stmts ::= _stmts (83)
        24     c_stmts ::= _stmts (83)
        24     c_stmts ::= _stmts (83)
        24     suite_stmts_opt ::= suite_stmts (83)
        24     c_suite_stmts ::= suite_stmts (83)
        24     c_suite_stmts_opt ::= c_suite_stmts (83)
        24     c_suite_stmts_opt ::= suite_stmts_opt (83)
L. 88: 152     expr ::= LOAD_GLOBAL (84)
L. 88: 152     return_expr ::= expr (84)
L. 88: 152     return_expr ::= expr (84)
L. 88: 152     return_expr ::= expr (84)
       154     expr ::= LOAD_FAST (85)
       156     expr ::= LOAD_STR (86)
       154-158 subscript ::= expr expr BINARY_SUBSCR (87)
       154     expr ::= subscript (87)
L. 88: 152-160 call ::= expr expr CALL_FUNCTION_1 (88)
L. 88: 152     expr ::= call (88)
L. 88: 152     return_expr ::= expr (88)
L. 88: 152     return_expr ::= expr (88)
L. 88: 152     return_expr ::= expr (88)
       162     store ::= STORE_FAST (89)
L. 88: 152-162 assign ::= expr store (89)
L. 88: 152     stmt ::= assign (89)
L. 88: 152     stmts ::= stmt (89)
L. 88: 152     c_stmt ::= stmt (89)
L. 88: 152     sstmt ::= stmt (89)
        24-162 stmts ::= stmts stmt (89)
L. 66:  24-162 stmts ::= stmts stmt (89)
        24-162 stmts ::= stmts stmt (89)
        24-162 stmts ::= stmts stmt (89)
L. 88: 152     _stmts ::= stmts (89)
L. 88: 152     c_stmts ::= c_stmt (89)
L. 84: 132-162 c_stmts ::= c_stmts c_stmt (89)
L. 83: 118-162 c_stmts ::= c_stmts c_stmt (89)
L. 80:  96-162 c_stmts ::= c_stmts c_stmt (89)
L. 78:  80-162 c_stmts ::= c_stmts c_stmt (89)
L. 76:  72-162 c_stmts ::= c_stmts c_stmt (89)
        32-162 c_stmts ::= c_stmts c_stmt (89)
L. 66:  24-162 c_stmts ::= c_stmts c_stmt (89)
L. 69:  28-162 c_stmts ::= c_stmts c_stmt (89)
        24-162 c_stmts ::= c_stmts c_stmt (89)
        24-162 c_stmts ::= c_stmts c_stmt (89)
        24-162 c_stmts ::= c_stmts c_stmt (89)
L. 88: 152     stmts ::= sstmt (89)
        24-162 stmts ::= stmts sstmt (89)
L. 66:  24-162 stmts ::= stmts sstmt (89)
        24-162 stmts ::= stmts sstmt (89)
        24-162 stmts ::= stmts sstmt (89)
        24     _stmts ::= stmts (89)
L. 66:  24     _stmts ::= stmts (89)
        24     _stmts ::= stmts (89)
        24     _stmts ::= stmts (89)
L. 88: 152     c_stmts ::= _stmts (89)
L. 88: 152     suite_stmts ::= _stmts (89)
L. 88: 152     c_stmts ::= _stmts (89)
L. 88: 152     else_suitec ::= c_stmts (89)
L. 69:  28-162 iflaststmtc ::= testexpr c_stmts (89)
Reduce iflaststmtc invalid by check
        32     c_stmts_opt ::= c_stmts (89)
        32     ifstmts_jumpc ::= c_stmts (89)
L. 69:  28-162 iflaststmtc ::= testexprc c_stmts (89)
Reduce iflaststmtc invalid by check
L. 69:  28     c_stmts_opt ::= c_stmts (89)
L. 66:  24-162 iflaststmtc ::= testexpr c_stmts (89)
Reduce iflaststmtc invalid by check
L. 69:  28     c_stmts_opt ::= c_stmts (89)
L. 69:  28     ifstmts_jumpc ::= c_stmts (89)
L. 66:  24-162 iflaststmtc ::= testexprc c_stmts (89)
Reduce iflaststmtc invalid by check
        24     c_suite_stmts ::= c_stmts (89)
        24     suite_stmts ::= _stmts (89)
        24     c_stmts ::= _stmts (89)
L. 66:  24     c_stmts ::= _stmts (89)
        24     c_stmts ::= _stmts (89)
        24     c_stmts ::= _stmts (89)
L. 88: 152     else_suite ::= suite_stmts (89)
L. 88: 152     else_suitec ::= suite_stmts (89)
L. 84: 132-162 ifelsestmtc ::= testexpr c_stmts_opt jb_cfs else_suitec (89)
Reduce ifelsestmtc invalid by check
L. 66:  24-162 if_and_elsestmtc ::= expr_pjif expr_pjif c_stmts jb_cfs else_suitec \e_opt_come_from_except (89)
Reduce if_and_elsestmtc invalid by check
L. 69:  28-162 ifelsestmtc ::= testexpr c_stmts_opt jb_cfs else_suitec (89)
Reduce ifelsestmtc invalid by check
L. 66:  24-162 ifelsestmtc ::= testexpr c_stmts_opt jb_cfs else_suitec (89)
Reduce ifelsestmtc invalid by check
L. 69:  28-162 ifstmtc ::= testexpr ifstmts_jumpc (89)
L. 69:  28-162 ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms (89)
Reduce ifstmtc invalid by check
L. 69:  28-162 if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms (89)
Reduce if_not_stmtc invalid by check
L. 66:  24-162 ifstmtc ::= testexpr ifstmts_jumpc (89)
Reduce ifstmtc invalid by check
L. 66:  24-162 ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms (89)
Reduce ifstmtc invalid by check
L. 66:  24-162 if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms (89)
        24     c_suite_stmts_opt ::= c_suite_stmts (89)
        24     suite_stmts_opt ::= suite_stmts (89)
        24     c_suite_stmts ::= suite_stmts (89)
L. 69:  28-162 ifelsestmtc ::= testexpr c_stmts come_froms else_suite (89)
Reduce ifelsestmtc invalid by check
L. 66:  24-162 ifelsestmtc ::= testexpr c_stmts come_froms else_suite (89)
Reduce ifelsestmtc invalid by check
L. 69:  28     c_stmt ::= ifstmtc (89)
L. 66:  24     c_stmt ::= if_not_stmtc (89)
        24     c_suite_stmts_opt ::= suite_stmts_opt (89)
L. 69:  28     c_stmts ::= c_stmt (89)
L. 66:  24     c_stmts ::= c_stmt (89)
L. 89: 164     expr ::= LOAD_GLOBAL (90)
L. 89: 164     return_expr ::= expr (90)
L. 89: 164     return_expr ::= expr (90)
L. 89: 164     return_expr ::= expr (90)
       166     expr ::= LOAD_FAST (91)
L. 89: 164-168 call ::= expr expr CALL_FUNCTION_1 (92)
L. 89: 164     expr ::= call (92)
L. 89: 164     return_expr ::= expr (92)
L. 89: 164     return_expr ::= expr (92)
L. 89: 164     return_expr ::= expr (92)
       170     expr ::= LOAD_CONST (93)
L. 89: 164-172 compare_single ::= expr expr COMPARE_OP (94)
L. 89: 164     compare ::= compare_single (94)
L. 89: 164     expr ::= compare (94)
L. 89: 164     return_expr ::= expr (94)
L. 89: 164     return_expr ::= expr (94)
L. 89: 164     return_expr ::= expr (94)
L. 89: 164-174 expr_pjif ::= expr POP_JUMP_IF_FALSE (95)
L. 89: 164-174 expr_pjif ::= expr POP_JUMP_IF_FALSE (95)
L. 89: 164     testfalse ::= expr_pjif (95)
L. 89: 164     and_parts ::= expr_pjif (95)
L. 89: 164     and_parts ::= expr_pjif (95)
L. 89: 164     testfalse ::= expr_pjif (95)
L. 89: 164     testexpr ::= testfalse (95)
L. 89: 164     testexprc ::= testexpr (95)
L. 89: 164     testexprc ::= testexpr (95)
L. 90: 176     expr ::= LOAD_GLOBAL (96)
L. 90: 176     return_expr ::= expr (96)
L. 90: 176-178 attribute37 ::= expr LOAD_METHOD (97)
L. 90: 176     expr ::= attribute37 (97)
L. 90: 176     return_expr ::= expr (97)
       180     expr ::= LOAD_STR (98)
L. 91: 182     expr ::= LOAD_STR (99)
       184     expr ::= LOAD_GLOBAL (100)
       186     expr ::= LOAD_FAST (101)
       184-188 call ::= expr expr CALL_FUNCTION_1 (102)
       184     expr ::= call (102)
       190     binary_operator ::= BINARY_MODULO (103)
L. 91: 182-190 bin_op ::= expr expr binary_operator (103)
L. 91: 182     expr ::= bin_op (103)
L. 90: 192     binary_operator ::= BINARY_ADD (104)
       180-192 bin_op ::= expr expr binary_operator (104)
       180     expr ::= bin_op (104)
L. 90: 176-194 call ::= expr expr CALL_METHOD_1 (105)
L. 90: 176     expr ::= call (105)
L. 90: 176     return_expr ::= expr (105)
L. 90: 176-196 expr_stmt ::= expr POP_TOP (106)
L. 90: 176     stmt ::= expr_stmt (106)
L. 90: 176     stmts ::= stmt (106)
L. 90: 176     c_stmt ::= stmt (106)
L. 90: 176     sstmt ::= stmt (106)
L. 89: 164-196 ifstmt ::= testexpr stmts \e__come_froms (106)
L. 89: 164-196 iflaststmt ::= testexpr stmts (106)
Reduce iflaststmt invalid by check
L. 90: 176     stmts_opt ::= stmts (106)
L. 90: 176     _stmts ::= stmts (106)
L. 90: 176     _stmts ::= stmts (106)
L. 90: 176     c_stmts ::= c_stmt (106)
L. 90: 176     stmts ::= sstmt (106)
L. 89: 164     stmt ::= ifstmt (106)
L. 90: 176     c_stmts ::= _stmts (106)
L. 90: 176     c_stmts ::= _stmts (106)
L. 89: 164-196 iflaststmtc ::= testexpr c_stmts (106)
Reduce iflaststmtc invalid by check
L. 90: 176     c_stmts_opt ::= c_stmts (106)
L. 90: 176     ifstmts_jumpc ::= c_stmts (106)
L. 89: 164-196 iflaststmtc ::= testexpr c_stmts (106)
Reduce iflaststmtc invalid by check
L. 90: 176     c_stmts_opt ::= c_stmts (106)
L. 89: 164-196 iflaststmtc ::= testexprc c_stmts (106)
Reduce iflaststmtc invalid by check
L. 88: 152-196 stmts ::= stmts stmt (106)
L. 89: 164     stmts ::= stmt (106)
L. 89: 164     c_stmt ::= stmt (106)
L. 89: 164     sstmt ::= stmt (106)
        24-196 stmts ::= stmts stmt (106)
L. 66:  24-196 stmts ::= stmts stmt (106)
        24-196 stmts ::= stmts stmt (106)
        24-196 stmts ::= stmts stmt (106)
L. 89: 164-196 ifstmtc ::= testexpr ifstmts_jumpc (106)
L. 89: 164-196 ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms (106)
L. 89: 164-196 if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms (106)
L. 88: 152     _stmts ::= stmts (106)
L. 89: 164     _stmts ::= stmts (106)
L. 89: 164     c_stmts ::= c_stmt (106)
L. 88: 152-196 c_stmts ::= c_stmts c_stmt (106)
L. 84: 132-196 c_stmts ::= c_stmts c_stmt (106)
L. 83: 118-196 c_stmts ::= c_stmts c_stmt (106)
L. 80:  96-196 c_stmts ::= c_stmts c_stmt (106)
L. 78:  80-196 c_stmts ::= c_stmts c_stmt (106)
L. 76:  72-196 c_stmts ::= c_stmts c_stmt (106)
        32-196 c_stmts ::= c_stmts c_stmt (106)
L. 66:  24-196 c_stmts ::= c_stmts c_stmt (106)
L. 69:  28-196 c_stmts ::= c_stmts c_stmt (106)
        24-196 c_stmts ::= c_stmts c_stmt (106)
        24-196 c_stmts ::= c_stmts c_stmt (106)
        24-196 c_stmts ::= c_stmts c_stmt (106)
L. 88: 152-196 stmts ::= stmts sstmt (106)
L. 89: 164     stmts ::= sstmt (106)
        24-196 stmts ::= stmts sstmt (106)
L. 66:  24-196 stmts ::= stmts sstmt (106)
        24-196 stmts ::= stmts sstmt (106)
        24-196 stmts ::= stmts sstmt (106)
        24     _stmts ::= stmts (106)
L. 66:  24     _stmts ::= stmts (106)
        24     _stmts ::= stmts (106)
        24     _stmts ::= stmts (106)
L. 89: 164     c_stmt ::= ifstmtc (106)
L. 89: 164     c_stmt ::= if_not_stmtc (106)
L. 88: 152     c_stmts ::= _stmts (106)
L. 88: 152     suite_stmts ::= _stmts (106)
L. 88: 152     c_stmts ::= _stmts (106)
L. 89: 164     c_stmts ::= _stmts (106)
L. 88: 152     else_suitec ::= c_stmts (106)
L. 69:  28-196 iflaststmtc ::= testexpr c_stmts (106)
Reduce iflaststmtc invalid by check
        32     c_stmts_opt ::= c_stmts (106)
        32     ifstmts_jumpc ::= c_stmts (106)
L. 69:  28-196 iflaststmtc ::= testexprc c_stmts (106)
Reduce iflaststmtc invalid by check
L. 69:  28     c_stmts_opt ::= c_stmts (106)
L. 66:  24-196 iflaststmtc ::= testexpr c_stmts (106)
Reduce iflaststmtc invalid by check
L. 69:  28     c_stmts_opt ::= c_stmts (106)
L. 69:  28     ifstmts_jumpc ::= c_stmts (106)
L. 66:  24-196 iflaststmtc ::= testexprc c_stmts (106)
Reduce iflaststmtc invalid by check
        24     c_suite_stmts ::= c_stmts (106)
        24     suite_stmts ::= _stmts (106)
        24     c_stmts ::= _stmts (106)
L. 66:  24     c_stmts ::= _stmts (106)
        24     c_stmts ::= _stmts (106)
        24     c_stmts ::= _stmts (106)
L. 88: 152     else_suite ::= suite_stmts (106)
L. 88: 152     else_suitec ::= suite_stmts (106)
L. 84: 132-196 ifelsestmtc ::= testexpr c_stmts_opt jb_cfs else_suitec (106)
L. 66:  24-196 if_and_elsestmtc ::= expr_pjif expr_pjif c_stmts jb_cfs else_suitec \e_opt_come_from_except (106)
Reduce if_and_elsestmtc invalid by check
L. 69:  28-196 ifelsestmtc ::= testexpr c_stmts_opt jb_cfs else_suitec (106)
Reduce ifelsestmtc invalid by check
L. 66:  24-196 ifelsestmtc ::= testexpr c_stmts_opt jb_cfs else_suitec (106)
Reduce ifelsestmtc invalid by check
L. 69:  28-196 ifstmtc ::= testexpr ifstmts_jumpc (106)
Reduce ifstmtc invalid by check
L. 69:  28-196 ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms (106)
Reduce ifstmtc invalid by check
L. 69:  28-196 if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms (106)
Reduce if_not_stmtc invalid by check
L. 66:  24-196 ifstmtc ::= testexpr ifstmts_jumpc (106)
L. 66:  24-196 ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms (106)
L. 66:  24-196 if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms (106)
        24     c_suite_stmts_opt ::= c_suite_stmts (106)
        24     suite_stmts_opt ::= suite_stmts (106)
        24     c_suite_stmts ::= suite_stmts (106)
L. 69:  28-196 ifelsestmtc ::= testexpr c_stmts come_froms else_suite (106)
Reduce ifelsestmtc invalid by check
L. 66:  24-196 ifelsestmtc ::= testexpr c_stmts come_froms else_suite (106)
Reduce ifelsestmtc invalid by check
L. 84: 132     lastc_stmt ::= ifelsestmtc (106)
L. 84: 132     c_stmt ::= ifelsestmtc (106)
L. 84: 132     lastc_stmt ::= ifelsestmtc (106)
L. 66:  24     c_stmt ::= ifstmtc (106)
L. 66:  24     c_stmt ::= if_not_stmtc (106)
        24     c_suite_stmts_opt ::= suite_stmts_opt (106)
L. 84: 132     c_stmts ::= lastc_stmt (106)
L. 76:  72-196 c_stmts ::= _stmts lastc_stmt (106)
L. 83: 118-196 c_stmts ::= _stmts lastc_stmt (106)
L. 80:  96-196 c_stmts ::= _stmts lastc_stmt (106)
L. 78:  80-196 c_stmts ::= _stmts lastc_stmt (106)
        32-196 c_stmts ::= _stmts lastc_stmt (106)
L. 69:  28-196 c_stmts ::= _stmts lastc_stmt (106)
L. 84: 132     c_stmts ::= c_stmt (106)
L. 66:  24     c_stmts ::= c_stmt (106)
L. 92: 198-198 whileTruestmt38 ::= \e__come_froms \e_pass JUMP_LOOP (107)
Reduce whileTruestmt38 invalid by check
L. 89: 164-198 whilestmt38 ::= \e__come_froms testexpr c_stmts JUMP_LOOP \e__come_froms (107)
Reduce whilestmt38 invalid by check
L. 89: 164-198 iflaststmtc ::= testexpr c_stmts JUMP_LOOP (107)
Reduce iflaststmtc invalid by check
L. 90: 176-198 ifstmts_jumpc ::= c_stmts JUMP_LOOP (107)
L. 90: 176-198 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP \e__come_froms (107)
Reduce whileTruestmt38 invalid by check
L. 89: 164-198 iflaststmtc ::= testexpr c_stmts JUMP_LOOP (107)
Reduce iflaststmtc invalid by check
L. 90: 176-198 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP \e__come_froms (107)
Reduce whileTruestmt38 invalid by check
L. 89: 164-198 iflaststmtc ::= testexprc c_stmts JUMP_LOOP \e_opt_pop_block (107)
Reduce iflaststmtc invalid by check
L. 89: 164-198 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP \e__come_froms (107)
Reduce whileTruestmt38 invalid by check
       152-198 whileTruestmt38 ::= _come_froms c_stmts JUMP_LOOP \e__come_froms (107)
Reduce whileTruestmt38 invalid by check
L. 88: 152-198 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP \e__come_froms (107)
Reduce whileTruestmt38 invalid by check
L. 84: 132-198 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP \e__come_froms (107)
Reduce whileTruestmt38 invalid by check
L. 83: 118-198 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP \e__come_froms (107)
Reduce whileTruestmt38 invalid by check
L. 80:  96-198 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP \e__come_froms (107)
Reduce whileTruestmt38 invalid by check
L. 78:  80-198 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP \e__come_froms (107)
Reduce whileTruestmt38 invalid by check
        72-198 whileTruestmt38 ::= _come_froms c_stmts JUMP_LOOP \e__come_froms (107)
Reduce whileTruestmt38 invalid by check
L. 76:  72-198 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP \e__come_froms (107)
Reduce whileTruestmt38 invalid by check
        72-198 whileTruestmt38 ::= _come_froms c_stmts JUMP_LOOP \e__come_froms (107)
Reduce whileTruestmt38 invalid by check
        32-198 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP \e__come_froms (107)
Reduce whileTruestmt38 invalid by check
L. 69:  28-198 whilestmt38 ::= \e__come_froms testexpr c_stmts JUMP_LOOP \e__come_froms (107)
Reduce whilestmt38 invalid by check
L. 69:  28-198 iflaststmtc ::= testexpr c_stmts JUMP_LOOP (107)
Reduce iflaststmtc invalid by check
        32-198 ifstmts_jumpc ::= c_stmts JUMP_LOOP (107)
        32-198 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP \e__come_froms (107)
Reduce whileTruestmt38 invalid by check
L. 69:  28-198 iflaststmtc ::= testexprc c_stmts JUMP_LOOP \e_opt_pop_block (107)
Reduce iflaststmtc invalid by check
        24-198 whileTruestmt38 ::= _come_froms c_stmts JUMP_LOOP \e__come_froms (107)
L. 66:  24-198 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP \e__come_froms (107)
        24-198 whileTruestmt38 ::= _come_froms c_stmts JUMP_LOOP \e__come_froms (107)
        24-198 whileTruestmt38 ::= _come_froms c_stmts JUMP_LOOP \e__come_froms (107)
        24-198 whilestmt38 ::= _come_froms testexpr c_stmts JUMP_LOOP \e__come_froms (107)
L. 69:  28-198 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP \e__come_froms (107)
Reduce whileTruestmt38 invalid by check
L. 66:  24-198 whilestmt38 ::= \e__come_froms testexpr c_stmts JUMP_LOOP \e__come_froms (107)
L. 66:  24-198 iflaststmtc ::= testexpr c_stmts JUMP_LOOP (107)
Reduce iflaststmtc invalid by check
L. 69:  28-198 ifstmts_jumpc ::= c_stmts JUMP_LOOP (107)
L. 69:  28-198 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP \e__come_froms (107)
Reduce whileTruestmt38 invalid by check
        24-198 whilestmt38 ::= _come_froms testexpr c_stmts JUMP_LOOP \e__come_froms (107)
        24-198 whilestmt38 ::= _come_froms testexpr c_stmts JUMP_LOOP \e__come_froms (107)
L. 66:  24-198 iflaststmtc ::= testexprc c_stmts JUMP_LOOP \e_opt_pop_block (107)
Reduce iflaststmtc invalid by check
        24-198 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP \e__come_froms (107)
        24-198 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP \e__come_froms (107)
        24-198 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP \e__come_froms (107)
L. 89: 164-198 ifstmtc ::= testexpr ifstmts_jumpc (107)
L. 89: 164-198 ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms (107)
L. 89: 164-198 if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms (107)
Reduce if_not_stmtc invalid by check
L. 69:  28-198 ifstmtc ::= testexpr ifstmts_jumpc (107)
L. 69:  28-198 ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms (107)
Reduce ifstmtc invalid by check
L. 69:  28-198 if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms (107)
Reduce if_not_stmtc invalid by check
        24     stmt ::= whileTruestmt38 (107)
L. 66:  24     stmt ::= whileTruestmt38 (107)
        24     stmt ::= whileTruestmt38 (107)
        24     stmt ::= whileTruestmt38 (107)
        24     stmt ::= whilestmt38 (107)
L. 66:  24     stmt ::= whilestmt38 (107)
L. 66:  24-198 ifstmtc ::= testexpr ifstmts_jumpc (107)
Reduce ifstmtc invalid by check
L. 66:  24-198 ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms (107)
Reduce ifstmtc invalid by check
L. 66:  24-198 if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms (107)
        24     stmt ::= whilestmt38 (107)
        24     stmt ::= whilestmt38 (107)
L. 89: 164     c_stmt ::= ifstmtc (107)
L. 69:  28     c_stmt ::= ifstmtc (107)
        24     stmts ::= stmt (107)
        24     c_stmt ::= stmt (107)
        24     sstmt ::= stmt (107)
L. 66:  24     stmts ::= stmt (107)
L. 66:  24     c_stmt ::= stmt (107)
L. 66:  24     sstmt ::= stmt (107)
        24     stmts ::= stmt (107)
        24     c_stmt ::= stmt (107)
        24     sstmt ::= stmt (107)
        24     stmts ::= stmt (107)
        24     c_stmt ::= stmt (107)
        24     sstmt ::= stmt (107)
L. 66:  24     c_stmt ::= if_not_stmtc (107)
L. 89: 164     c_stmts ::= c_stmt (107)
L. 88: 152-198 c_stmts ::= c_stmts c_stmt (107)
L. 84: 132-198 c_stmts ::= c_stmts c_stmt (107)
L. 83: 118-198 c_stmts ::= c_stmts c_stmt (107)
L. 80:  96-198 c_stmts ::= c_stmts c_stmt (107)
L. 78:  80-198 c_stmts ::= c_stmts c_stmt (107)
L. 76:  72-198 c_stmts ::= c_stmts c_stmt (107)
        32-198 c_stmts ::= c_stmts c_stmt (107)
L. 66:  24-198 c_stmts ::= c_stmts c_stmt (107)
L. 69:  28-198 c_stmts ::= c_stmts c_stmt (107)
        24-198 c_stmts ::= c_stmts c_stmt (107)
        24-198 c_stmts ::= c_stmts c_stmt (107)
        24-198 c_stmts ::= c_stmts c_stmt (107)
L. 69:  28     c_stmts ::= c_stmt (107)
        24     _stmts ::= stmts (107)
        24     c_stmts ::= c_stmt (107)
        24     stmts ::= sstmt (107)
L. 66:  24     _stmts ::= stmts (107)
L. 66:  24     c_stmts ::= c_stmt (107)
L. 66:  24     stmts ::= sstmt (107)
        24     _stmts ::= stmts (107)
        24     c_stmts ::= c_stmt (107)
        24     stmts ::= sstmt (107)
        24     _stmts ::= stmts (107)
        24     c_stmts ::= c_stmt (107)
        24     stmts ::= sstmt (107)
L. 88: 152     else_suitec ::= c_stmts (107)
L. 69:  28-198 iflaststmtc ::= testexpr c_stmts (107)
Reduce iflaststmtc invalid by check
        32     c_stmts_opt ::= c_stmts (107)
        32     ifstmts_jumpc ::= c_stmts (107)
L. 69:  28-198 iflaststmtc ::= testexprc c_stmts (107)
Reduce iflaststmtc invalid by check
L. 69:  28     c_stmts_opt ::= c_stmts (107)
L. 66:  24-198 iflaststmtc ::= testexpr c_stmts (107)
Reduce iflaststmtc invalid by check
L. 69:  28     c_stmts_opt ::= c_stmts (107)
L. 69:  28     ifstmts_jumpc ::= c_stmts (107)
L. 66:  24-198 iflaststmtc ::= testexprc c_stmts (107)
Reduce iflaststmtc invalid by check
        24     c_suite_stmts ::= c_stmts (107)
        24     suite_stmts ::= _stmts (107)
        24     c_stmts ::= _stmts (107)
L. 66:  24     c_stmts ::= _stmts (107)
        24     c_stmts ::= _stmts (107)
        24     c_stmts ::= _stmts (107)
L. 84: 132-198 ifelsestmtc ::= testexpr c_stmts_opt jb_cfs else_suitec (107)
L. 66:  24-198 if_and_elsestmtc ::= expr_pjif expr_pjif c_stmts jb_cfs else_suitec \e_opt_come_from_except (107)
Reduce if_and_elsestmtc invalid by check
L. 69:  28-198 ifelsestmtc ::= testexpr c_stmts_opt jb_cfs else_suitec (107)
Reduce ifelsestmtc invalid by check
L. 66:  24-198 ifelsestmtc ::= testexpr c_stmts_opt jb_cfs else_suitec (107)
Reduce ifelsestmtc invalid by check
        24     c_suite_stmts_opt ::= c_suite_stmts (107)
        24     suite_stmts_opt ::= suite_stmts (107)
        24     c_suite_stmts ::= suite_stmts (107)
L. 84: 132     lastc_stmt ::= ifelsestmtc (107)
L. 84: 132     c_stmt ::= ifelsestmtc (107)
L. 84: 132     lastc_stmt ::= ifelsestmtc (107)
        24     c_suite_stmts_opt ::= suite_stmts_opt (107)
L. 84: 132     c_stmts ::= lastc_stmt (107)
L. 76:  72-198 c_stmts ::= _stmts lastc_stmt (107)
L. 83: 118-198 c_stmts ::= _stmts lastc_stmt (107)
L. 80:  96-198 c_stmts ::= _stmts lastc_stmt (107)
L. 78:  80-198 c_stmts ::= _stmts lastc_stmt (107)
        32-198 c_stmts ::= _stmts lastc_stmt (107)
L. 69:  28-198 c_stmts ::= _stmts lastc_stmt (107)
L. 84: 132     c_stmts ::= c_stmt (107)
       200-200 _come_froms ::= \e__come_froms COME_FROM (108)
       200     come_froms ::= COME_FROM (108)
       200-200 _come_froms ::= \e__come_froms COME_FROM (108)
       200     come_froms ::= COME_FROM (108)
       200     come_from_opt ::= COME_FROM (108)
       200     come_froms ::= COME_FROM (108)
       200     come_any_from ::= COME_FROM (108)
       200     come_from_opt ::= COME_FROM (108)
       200     come_froms ::= COME_FROM (108)
L. 89: 164-200 whilestmt38 ::= \e__come_froms testexpr c_stmts JUMP_LOOP _come_froms (108)
Reduce whilestmt38 invalid by check
L. 90: 176-200 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP _come_froms (108)
Reduce whileTruestmt38 invalid by check
L. 89: 164-200 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP _come_froms (108)
Reduce whileTruestmt38 invalid by check
       152-200 whileTruestmt38 ::= _come_froms c_stmts JUMP_LOOP _come_froms (108)
Reduce whileTruestmt38 invalid by check
L. 88: 152-200 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP _come_froms (108)
Reduce whileTruestmt38 invalid by check
L. 84: 132-200 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP _come_froms (108)
Reduce whileTruestmt38 invalid by check
L. 83: 118-200 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP _come_froms (108)
Reduce whileTruestmt38 invalid by check
L. 80:  96-200 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP _come_froms (108)
Reduce whileTruestmt38 invalid by check
L. 78:  80-200 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP _come_froms (108)
Reduce whileTruestmt38 invalid by check
        72-200 whileTruestmt38 ::= _come_froms c_stmts JUMP_LOOP _come_froms (108)
Reduce whileTruestmt38 invalid by check
L. 76:  72-200 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP _come_froms (108)
Reduce whileTruestmt38 invalid by check
        72-200 whileTruestmt38 ::= _come_froms c_stmts JUMP_LOOP _come_froms (108)
Reduce whileTruestmt38 invalid by check
        32-200 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP _come_froms (108)
Reduce whileTruestmt38 invalid by check
L. 69:  28-200 whilestmt38 ::= \e__come_froms testexpr c_stmts JUMP_LOOP _come_froms (108)
Reduce whilestmt38 invalid by check
        24-200 whileTruestmt38 ::= _come_froms c_stmts JUMP_LOOP _come_froms (108)
L. 66:  24-200 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP _come_froms (108)
        24-200 whileTruestmt38 ::= _come_froms c_stmts JUMP_LOOP _come_froms (108)
        24-200 whileTruestmt38 ::= _come_froms c_stmts JUMP_LOOP _come_froms (108)
        24-200 whilestmt38 ::= _come_froms testexpr c_stmts JUMP_LOOP _come_froms (108)
L. 69:  28-200 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP _come_froms (108)
Reduce whileTruestmt38 invalid by check
L. 66:  24-200 whilestmt38 ::= \e__come_froms testexpr c_stmts JUMP_LOOP _come_froms (108)
        24-200 whilestmt38 ::= _come_froms testexpr c_stmts JUMP_LOOP _come_froms (108)
        24-200 whilestmt38 ::= _come_froms testexpr c_stmts JUMP_LOOP _come_froms (108)
        24-200 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP _come_froms (108)
        24-200 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP _come_froms (108)
        24-200 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP _come_froms (108)
L. 89: 164-200 ifstmtc ::= testexprc ifstmts_jumpc _come_froms (108)
L. 89: 164-200 if_not_stmtc ::= testexprc ifstmts_jumpc _come_froms (108)
Reduce if_not_stmtc invalid by check
L. 69:  28-200 ifstmtc ::= testexprc ifstmts_jumpc _come_froms (108)
L. 69:  28-200 if_not_stmtc ::= testexprc ifstmts_jumpc _come_froms (108)
Reduce if_not_stmtc invalid by check
L. 66:  24-200 ifstmtc ::= testexprc ifstmts_jumpc _come_froms (108)
Reduce ifstmtc invalid by check
L. 66:  24-200 if_not_stmtc ::= testexprc ifstmts_jumpc _come_froms (108)
L. 89: 164-200 whilestmt38 ::= \e__come_froms testexpr c_stmts_opt JUMP_LOOP come_froms (108)
Reduce whilestmt38 invalid by check
L. 92: 198-200 jb_cfs ::= \e_come_from_opt JUMP_LOOP come_froms (108)
L. 84: 132-200 ifelsestmtc ::= testexpr c_stmts_opt jb_cfs else_suitec JUMP_LOOP come_froms (108)
Reduce ifelsestmtc invalid by check
L. 69:  28-200 ifelsestmtc ::= testexpr c_stmts_opt jb_cfs else_suitec JUMP_LOOP come_froms (108)
Reduce ifelsestmtc invalid by check
L. 66:  24-200 ifelsestmtc ::= testexpr c_stmts_opt jb_cfs else_suitec JUMP_LOOP come_froms (108)
Reduce ifelsestmtc invalid by check
L. 69:  28-200 whilestmt38 ::= \e__come_froms testexpr c_stmts_opt JUMP_LOOP come_froms (108)
Reduce whilestmt38 invalid by check
        24-200 whilestmt38 ::= _come_froms testexpr c_stmts_opt JUMP_LOOP come_froms (108)
L. 66:  24-200 whilestmt38 ::= \e__come_froms testexpr c_stmts_opt JUMP_LOOP come_froms (108)
        24-200 whilestmt38 ::= _come_froms testexpr c_stmts_opt JUMP_LOOP come_froms (108)
        24-200 whilestmt38 ::= _come_froms testexpr c_stmts_opt JUMP_LOOP come_froms (108)
L. 69:  28-200 whilestmt38 ::= \e__come_froms testexpr c_stmts come_froms (108)
Reduce whilestmt38 invalid by check
L. 69:  28-200 iflaststmtc ::= testexpr c_stmts come_froms (108)
Reduce iflaststmtc invalid by check
        24-200 whilestmt38 ::= _come_froms testexpr c_stmts come_froms (108)
L. 66:  24-200 whilestmt38 ::= \e__come_froms testexpr c_stmts come_froms (108)
L. 66:  24-200 iflaststmtc ::= testexpr c_stmts come_froms (108)
Reduce iflaststmtc invalid by check
        24-200 whilestmt38 ::= _come_froms testexpr c_stmts come_froms (108)
        24-200 whilestmt38 ::= _come_froms testexpr c_stmts come_froms (108)
        32-200 ifstmts_jumpc ::= c_stmts_opt come_froms (108)
L. 69:  28-200 ifstmts_jumpc ::= c_stmts_opt come_froms (108)
       200     come_any_froms ::= come_any_from (108)
        24     stmt ::= whileTruestmt38 (108)
L. 66:  24     stmt ::= whileTruestmt38 (108)
        24     stmt ::= whileTruestmt38 (108)
        24     stmt ::= whileTruestmt38 (108)
        24     stmt ::= whilestmt38 (108)
L. 66:  24     stmt ::= whilestmt38 (108)
        24     stmt ::= whilestmt38 (108)
        24     stmt ::= whilestmt38 (108)
L. 89: 164     c_stmt ::= ifstmtc (108)
L. 69:  28     c_stmt ::= ifstmtc (108)
L. 66:  24     c_stmt ::= if_not_stmtc (108)
L. 69:  28-200 ifstmtc ::= testexpr ifstmts_jumpc (108)
L. 69:  28-200 ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms (108)
Reduce ifstmtc invalid by check
L. 69:  28-200 if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms (108)
Reduce if_not_stmtc invalid by check
L. 66:  24-200 ifstmtc ::= testexpr ifstmts_jumpc (108)
Reduce ifstmtc invalid by check
L. 66:  24-200 ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms (108)
Reduce ifstmtc invalid by check
L. 66:  24-200 if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms (108)
       200     opt_come_from_except ::= come_any_froms (108)
        24     stmts ::= stmt (108)
        24     c_stmt ::= stmt (108)
        24     sstmt ::= stmt (108)
L. 66:  24     stmts ::= stmt (108)
L. 66:  24     c_stmt ::= stmt (108)
L. 66:  24     sstmt ::= stmt (108)
        24     stmts ::= stmt (108)
        24     c_stmt ::= stmt (108)
        24     sstmt ::= stmt (108)
        24     stmts ::= stmt (108)
        24     c_stmt ::= stmt (108)
        24     sstmt ::= stmt (108)
L. 89: 164     c_stmts ::= c_stmt (108)
L. 88: 152-200 c_stmts ::= c_stmts c_stmt (108)
L. 84: 132-200 c_stmts ::= c_stmts c_stmt (108)
L. 83: 118-200 c_stmts ::= c_stmts c_stmt (108)
L. 80:  96-200 c_stmts ::= c_stmts c_stmt (108)
L. 78:  80-200 c_stmts ::= c_stmts c_stmt (108)
L. 76:  72-200 c_stmts ::= c_stmts c_stmt (108)
        32-200 c_stmts ::= c_stmts c_stmt (108)
L. 66:  24-200 c_stmts ::= c_stmts c_stmt (108)
L. 69:  28-200 c_stmts ::= c_stmts c_stmt (108)
        24-200 c_stmts ::= c_stmts c_stmt (108)
        24-200 c_stmts ::= c_stmts c_stmt (108)
        24-200 c_stmts ::= c_stmts c_stmt (108)
L. 69:  28     c_stmts ::= c_stmt (108)
L. 66:  24     c_stmts ::= c_stmt (108)
L. 66:  24-200 if_and_elsestmtc ::= expr_pjif expr_pjif c_stmts jb_cfs else_suitec opt_come_from_except (108)
Reduce if_and_elsestmtc invalid by check
        24     _stmts ::= stmts (108)
        24     c_stmts ::= c_stmt (108)
        24     stmts ::= sstmt (108)
L. 66:  24     _stmts ::= stmts (108)
L. 66:  24     stmts ::= sstmt (108)
        24     _stmts ::= stmts (108)
        24     c_stmts ::= c_stmt (108)
        24     stmts ::= sstmt (108)
        24     _stmts ::= stmts (108)
        24     c_stmts ::= c_stmt (108)
        24     stmts ::= sstmt (108)
L. 88: 152     else_suitec ::= c_stmts (108)
L. 69:  28-200 iflaststmtc ::= testexpr c_stmts (108)
Reduce iflaststmtc invalid by check
        32     c_stmts_opt ::= c_stmts (108)
        32     ifstmts_jumpc ::= c_stmts (108)
L. 69:  28-200 iflaststmtc ::= testexprc c_stmts (108)
Reduce iflaststmtc invalid by check
L. 69:  28     c_stmts_opt ::= c_stmts (108)
L. 66:  24-200 iflaststmtc ::= testexpr c_stmts (108)
Reduce iflaststmtc invalid by check
L. 69:  28     c_stmts_opt ::= c_stmts (108)
L. 69:  28     ifstmts_jumpc ::= c_stmts (108)
L. 66:  24-200 iflaststmtc ::= testexprc c_stmts (108)
Reduce iflaststmtc invalid by check
        24     c_suite_stmts ::= c_stmts (108)
        24     suite_stmts ::= _stmts (108)
        24     c_stmts ::= _stmts (108)
L. 66:  24     c_stmts ::= _stmts (108)
        24     c_stmts ::= _stmts (108)
        24     c_stmts ::= _stmts (108)
L. 84: 132-200 ifelsestmtc ::= testexpr c_stmts_opt jb_cfs else_suitec (108)
Reduce ifelsestmtc invalid by check
L. 66:  24-200 if_and_elsestmtc ::= expr_pjif expr_pjif c_stmts jb_cfs else_suitec \e_opt_come_from_except (108)
Reduce if_and_elsestmtc invalid by check
L. 69:  28-200 ifelsestmtc ::= testexpr c_stmts_opt jb_cfs else_suitec (108)
Reduce ifelsestmtc invalid by check
L. 66:  24-200 ifelsestmtc ::= testexpr c_stmts_opt jb_cfs else_suitec (108)
Reduce ifelsestmtc invalid by check
        24     c_suite_stmts_opt ::= c_suite_stmts (108)
        24     suite_stmts_opt ::= suite_stmts (108)
        24     c_suite_stmts ::= suite_stmts (108)
        24     c_suite_stmts_opt ::= suite_stmts_opt (108)
L. 94: 200     expr ::= LOAD_FAST (109)
L. 94: 200     return_expr ::= expr (109)
L. 94: 200     return_expr ::= expr (109)
L. 94: 200     return_expr ::= expr (109)
       202     expr ::= LOAD_CONST (110)
L. 94: 200-204 subscript ::= expr expr BINARY_SUBSCR (111)
L. 94: 200     expr ::= subscript (111)
L. 94: 200     return_expr ::= expr (111)
L. 94: 200     return_expr ::= expr (111)
L. 94: 200     return_expr ::= expr (111)
       206     expr ::= LOAD_CONST (112)
       208     binary_operator ::= BINARY_AND (113)
L. 94: 200-208 bin_op ::= expr expr binary_operator (113)
L. 94: 200     expr ::= bin_op (113)
L. 94: 200     return_expr ::= expr (113)
L. 94: 200     return_expr ::= expr (113)
L. 94: 200     return_expr ::= expr (113)
L. 94: 200-210 expr_pjif ::= expr POP_JUMP_IF_FALSE (114)
L. 94: 200-210 expr_pjif ::= expr POP_JUMP_IF_FALSE (114)
L. 94: 200     testfalse ::= expr_pjif (114)
L. 94: 200     and_parts ::= expr_pjif (114)
L. 94: 200     and_parts ::= expr_pjif (114)
L. 94: 200     testfalse ::= expr_pjif (114)
L. 94: 200     testexpr ::= testfalse (114)
L. 94: 200     testexprc ::= testexpr (114)
L. 94: 200     testexprc ::= testexpr (114)
       212     expr ::= LOAD_CONST (115)
       212     expr ::= LOAD_CONST (115)
       212     return_expr ::= expr (115)
       214-214 jump_forward_else ::= JUMP_FORWARD \e__come_froms (116)
       214-216 jf_cf ::= JUMP_FORWARD COME_FROM (117)
       216-216 _come_froms ::= \e__come_froms COME_FROM (117)
       214-216 jump_forward_else ::= JUMP_FORWARD _come_froms (117)
       216     expr ::= LOAD_CONST (118)
L. 94: 200-216 if_exp ::= expr_pjif expr jump_forward_else expr (118)
L. 94: 200     expr ::= if_exp (118)
L. 94: 200     return_expr ::= expr (118)
L. 94: 200     return_expr ::= expr (118)
L. 94: 200     return_expr ::= expr (118)
L. 94: 200-218 if_exp ::= expr_pjif expr jf_cf expr COME_FROM (119)
       218     come_froms ::= COME_FROM (119)
L. 94: 200     expr ::= if_exp (119)
L. 94: 200-218 if_exp ::= expr_pjif expr jump_forward_else expr come_froms (119)
L. 94: 200     return_expr ::= expr (119)
L. 94: 200     return_expr ::= expr (119)
L. 94: 200     return_expr ::= expr (119)
       218     expr ::= LOAD_FAST (120)
       218-220 store ::= expr STORE_ATTR (121)
L. 94: 200-220 assign ::= expr store (121)
L. 94: 200     stmt ::= assign (121)
L. 94: 200     stmts ::= stmt (121)
L. 94: 200     c_stmt ::= stmt (121)
L. 94: 200     sstmt ::= stmt (121)
        24-220 stmts ::= stmts stmt (121)
L. 66:  24-220 stmts ::= stmts stmt (121)
        24-220 stmts ::= stmts stmt (121)
        24-220 stmts ::= stmts stmt (121)
L. 94: 200     _stmts ::= stmts (121)
L. 94: 200     c_stmts ::= c_stmt (121)
L. 89: 164-220 c_stmts ::= c_stmts c_stmt (121)
L. 88: 152-220 c_stmts ::= c_stmts c_stmt (121)
L. 84: 132-220 c_stmts ::= c_stmts c_stmt (121)
L. 83: 118-220 c_stmts ::= c_stmts c_stmt (121)
L. 80:  96-220 c_stmts ::= c_stmts c_stmt (121)
L. 78:  80-220 c_stmts ::= c_stmts c_stmt (121)
L. 76:  72-220 c_stmts ::= c_stmts c_stmt (121)
        32-220 c_stmts ::= c_stmts c_stmt (121)
L. 66:  24-220 c_stmts ::= c_stmts c_stmt (121)
L. 69:  28-220 c_stmts ::= c_stmts c_stmt (121)
        24-220 c_stmts ::= c_stmts c_stmt (121)
        24-220 c_stmts ::= c_stmts c_stmt (121)
        24-220 c_stmts ::= c_stmts c_stmt (121)
L. 94: 200     stmts ::= sstmt (121)
        24-220 stmts ::= stmts sstmt (121)
L. 66:  24-220 stmts ::= stmts sstmt (121)
        24-220 stmts ::= stmts sstmt (121)
        24-220 stmts ::= stmts sstmt (121)
        24     _stmts ::= stmts (121)
L. 66:  24     _stmts ::= stmts (121)
        24     _stmts ::= stmts (121)
        24     _stmts ::= stmts (121)
L. 94: 200     c_stmts ::= _stmts (121)
L. 94: 200     suite_stmts ::= _stmts (121)
L. 94: 200     c_stmts ::= _stmts (121)
L. 94: 200     else_suitec ::= c_stmts (121)
L. 88: 152     else_suitec ::= c_stmts (121)
L. 69:  28-220 iflaststmtc ::= testexpr c_stmts (121)
Reduce iflaststmtc invalid by check
        32     c_stmts_opt ::= c_stmts (121)
        32     ifstmts_jumpc ::= c_stmts (121)
L. 69:  28-220 iflaststmtc ::= testexprc c_stmts (121)
Reduce iflaststmtc invalid by check
L. 69:  28     c_stmts_opt ::= c_stmts (121)
L. 66:  24-220 iflaststmtc ::= testexpr c_stmts (121)
Reduce iflaststmtc invalid by check
L. 69:  28     c_stmts_opt ::= c_stmts (121)
L. 69:  28     ifstmts_jumpc ::= c_stmts (121)
L. 66:  24-220 iflaststmtc ::= testexprc c_stmts (121)
Reduce iflaststmtc invalid by check
        24     c_suite_stmts ::= c_stmts (121)
        24     suite_stmts ::= _stmts (121)
        24     c_stmts ::= _stmts (121)
L. 66:  24     c_stmts ::= _stmts (121)
        24     c_stmts ::= _stmts (121)
        24     c_stmts ::= _stmts (121)
L. 94: 200     else_suite ::= suite_stmts (121)
L. 94: 200     else_suitec ::= suite_stmts (121)
L. 89: 164-220 ifelsestmtc ::= testexpr c_stmts_opt jb_cfs else_suitec (121)
Reduce ifelsestmtc invalid by check
L. 66:  24-220 if_and_elsestmtc ::= expr_pjif expr_pjif c_stmts jb_cfs else_suitec \e_opt_come_from_except (121)
Reduce if_and_elsestmtc invalid by check
L. 69:  28-220 ifelsestmtc ::= testexpr c_stmts_opt jb_cfs else_suitec (121)
Reduce ifelsestmtc invalid by check
L. 66:  24-220 ifelsestmtc ::= testexpr c_stmts_opt jb_cfs else_suitec (121)
Reduce ifelsestmtc invalid by check
L. 84: 132-220 ifelsestmtc ::= testexpr c_stmts_opt jb_cfs else_suitec (121)
Reduce ifelsestmtc invalid by check
L. 69:  28-220 ifstmtc ::= testexpr ifstmts_jumpc (121)
L. 69:  28-220 ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms (121)
Reduce ifstmtc invalid by check
L. 69:  28-220 if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms (121)
Reduce if_not_stmtc invalid by check
L. 66:  24-220 ifstmtc ::= testexpr ifstmts_jumpc (121)
Reduce ifstmtc invalid by check
L. 66:  24-220 ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms (121)
Reduce ifstmtc invalid by check
L. 66:  24-220 if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms (121)
        24     c_suite_stmts_opt ::= c_suite_stmts (121)
        24     suite_stmts_opt ::= suite_stmts (121)
        24     c_suite_stmts ::= suite_stmts (121)
L. 69:  28-220 ifelsestmtc ::= testexpr c_stmts come_froms else_suite (121)
Reduce ifelsestmtc invalid by check
L. 66:  24-220 ifelsestmtc ::= testexpr c_stmts come_froms else_suite (121)
Reduce ifelsestmtc invalid by check
L. 69:  28     c_stmt ::= ifstmtc (121)
L. 66:  24     c_stmt ::= if_not_stmtc (121)
        24     c_suite_stmts_opt ::= suite_stmts_opt (121)
L. 69:  28     c_stmts ::= c_stmt (121)
L. 66:  24     c_stmts ::= c_stmt (121)
L. 95: 222     expr ::= LOAD_FAST (122)
L. 95: 222     return_expr ::= expr (122)
L. 95: 222     return_expr ::= expr (122)
L. 95: 222     return_expr ::= expr (122)
       224     expr ::= LOAD_CONST (123)
L. 95: 222-226 subscript ::= expr expr BINARY_SUBSCR (124)
L. 95: 222     expr ::= subscript (124)
L. 95: 222     return_expr ::= expr (124)
L. 95: 222     return_expr ::= expr (124)
L. 95: 222     return_expr ::= expr (124)
       228     expr ::= LOAD_CONST (125)
       230     binary_operator ::= BINARY_AND (126)
L. 95: 222-230 bin_op ::= expr expr binary_operator (126)
L. 95: 222     expr ::= bin_op (126)
L. 95: 222     return_expr ::= expr (126)
L. 95: 222     return_expr ::= expr (126)
L. 95: 222     return_expr ::= expr (126)
L. 95: 222-232 expr_pjif ::= expr POP_JUMP_IF_FALSE (127)
L. 95: 222-232 expr_pjif ::= expr POP_JUMP_IF_FALSE (127)
L. 95: 222     testfalse ::= expr_pjif (127)
L. 95: 222     and_parts ::= expr_pjif (127)
L. 95: 222     and_parts ::= expr_pjif (127)
L. 95: 222     testfalse ::= expr_pjif (127)
L. 95: 222     testexpr ::= testfalse (127)
L. 95: 222     testexprc ::= testexpr (127)
L. 95: 222     testexprc ::= testexpr (127)
       234     expr ::= LOAD_CONST (128)
       234     expr ::= LOAD_CONST (128)
       234     return_expr ::= expr (128)
       236-236 jump_forward_else ::= JUMP_FORWARD \e__come_froms (129)
       236-238 jf_cf ::= JUMP_FORWARD COME_FROM (130)
       238-238 _come_froms ::= \e__come_froms COME_FROM (130)
       236-238 jump_forward_else ::= JUMP_FORWARD _come_froms (130)
       238     expr ::= LOAD_CONST (131)
L. 95: 222-238 if_exp ::= expr_pjif expr jump_forward_else expr (131)
L. 95: 222     expr ::= if_exp (131)
L. 95: 222     return_expr ::= expr (131)
L. 95: 222     return_expr ::= expr (131)
L. 95: 222     return_expr ::= expr (131)
L. 95: 222-240 if_exp ::= expr_pjif expr jf_cf expr COME_FROM (132)
       240     come_froms ::= COME_FROM (132)
L. 95: 222     expr ::= if_exp (132)
L. 95: 222-240 if_exp ::= expr_pjif expr jump_forward_else expr come_froms (132)
L. 95: 222     return_expr ::= expr (132)
L. 95: 222     return_expr ::= expr (132)
L. 95: 222     return_expr ::= expr (132)
       240     store ::= STORE_FAST (133)
L. 95: 222-240 assign ::= expr store (133)
L. 95: 222     stmt ::= assign (133)
L. 94: 200-240 stmts ::= stmts stmt (133)
L. 95: 222     stmts ::= stmt (133)
L. 95: 222     c_stmt ::= stmt (133)
L. 95: 222     sstmt ::= stmt (133)
        24-240 stmts ::= stmts stmt (133)
L. 66:  24-240 stmts ::= stmts stmt (133)
        24-240 stmts ::= stmts stmt (133)
        24-240 stmts ::= stmts stmt (133)
L. 94: 200     _stmts ::= stmts (133)
L. 95: 222     _stmts ::= stmts (133)
L. 95: 222     c_stmts ::= c_stmt (133)
L. 94: 200-240 c_stmts ::= c_stmts c_stmt (133)
L. 89: 164-240 c_stmts ::= c_stmts c_stmt (133)
L. 88: 152-240 c_stmts ::= c_stmts c_stmt (133)
L. 84: 132-240 c_stmts ::= c_stmts c_stmt (133)
L. 83: 118-240 c_stmts ::= c_stmts c_stmt (133)
L. 80:  96-240 c_stmts ::= c_stmts c_stmt (133)
L. 78:  80-240 c_stmts ::= c_stmts c_stmt (133)
L. 76:  72-240 c_stmts ::= c_stmts c_stmt (133)
        32-240 c_stmts ::= c_stmts c_stmt (133)
L. 66:  24-240 c_stmts ::= c_stmts c_stmt (133)
L. 69:  28-240 c_stmts ::= c_stmts c_stmt (133)
        24-240 c_stmts ::= c_stmts c_stmt (133)
        24-240 c_stmts ::= c_stmts c_stmt (133)
        24-240 c_stmts ::= c_stmts c_stmt (133)
L. 94: 200-240 stmts ::= stmts sstmt (133)
L. 95: 222     stmts ::= sstmt (133)
        24-240 stmts ::= stmts sstmt (133)
L. 66:  24-240 stmts ::= stmts sstmt (133)
        24-240 stmts ::= stmts sstmt (133)
        24-240 stmts ::= stmts sstmt (133)
        24     _stmts ::= stmts (133)
L. 66:  24     _stmts ::= stmts (133)
        24     _stmts ::= stmts (133)
        24     _stmts ::= stmts (133)
L. 94: 200     c_stmts ::= _stmts (133)
L. 94: 200     suite_stmts ::= _stmts (133)
L. 94: 200     c_stmts ::= _stmts (133)
L. 95: 222     c_stmts ::= _stmts (133)
L. 94: 200     else_suitec ::= c_stmts (133)
L. 88: 152     else_suitec ::= c_stmts (133)
L. 69:  28-240 iflaststmtc ::= testexpr c_stmts (133)
Reduce iflaststmtc invalid by check
        32     c_stmts_opt ::= c_stmts (133)
        32     ifstmts_jumpc ::= c_stmts (133)
L. 69:  28-240 iflaststmtc ::= testexprc c_stmts (133)
Reduce iflaststmtc invalid by check
L. 69:  28     c_stmts_opt ::= c_stmts (133)
L. 66:  24-240 iflaststmtc ::= testexpr c_stmts (133)
Reduce iflaststmtc invalid by check
L. 69:  28     c_stmts_opt ::= c_stmts (133)
L. 69:  28     ifstmts_jumpc ::= c_stmts (133)
L. 66:  24-240 iflaststmtc ::= testexprc c_stmts (133)
Reduce iflaststmtc invalid by check
        24     c_suite_stmts ::= c_stmts (133)
        24     suite_stmts ::= _stmts (133)
        24     c_stmts ::= _stmts (133)
L. 66:  24     c_stmts ::= _stmts (133)
        24     c_stmts ::= _stmts (133)
        24     c_stmts ::= _stmts (133)
L. 94: 200     else_suite ::= suite_stmts (133)
L. 94: 200     else_suitec ::= suite_stmts (133)
L. 89: 164-240 ifelsestmtc ::= testexpr c_stmts_opt jb_cfs else_suitec (133)
L. 66:  24-240 if_and_elsestmtc ::= expr_pjif expr_pjif c_stmts jb_cfs else_suitec \e_opt_come_from_except (133)
Reduce if_and_elsestmtc invalid by check
L. 69:  28-240 ifelsestmtc ::= testexpr c_stmts_opt jb_cfs else_suitec (133)
Reduce ifelsestmtc invalid by check
L. 66:  24-240 ifelsestmtc ::= testexpr c_stmts_opt jb_cfs else_suitec (133)
Reduce ifelsestmtc invalid by check
L. 84: 132-240 ifelsestmtc ::= testexpr c_stmts_opt jb_cfs else_suitec (133)
L. 69:  28-240 ifstmtc ::= testexpr ifstmts_jumpc (133)
L. 69:  28-240 ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms (133)
Reduce ifstmtc invalid by check
L. 69:  28-240 if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms (133)
Reduce if_not_stmtc invalid by check
L. 66:  24-240 ifstmtc ::= testexpr ifstmts_jumpc (133)
L. 66:  24-240 ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms (133)
L. 66:  24-240 if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms (133)
        24     c_suite_stmts_opt ::= c_suite_stmts (133)
        24     suite_stmts_opt ::= suite_stmts (133)
        24     c_suite_stmts ::= suite_stmts (133)
L. 69:  28-240 ifelsestmtc ::= testexpr c_stmts come_froms else_suite (133)
Reduce ifelsestmtc invalid by check
L. 66:  24-240 ifelsestmtc ::= testexpr c_stmts come_froms else_suite (133)
Reduce ifelsestmtc invalid by check
L. 89: 164     lastc_stmt ::= ifelsestmtc (133)
L. 89: 164     c_stmt ::= ifelsestmtc (133)
L. 89: 164     lastc_stmt ::= ifelsestmtc (133)
L. 84: 132     lastc_stmt ::= ifelsestmtc (133)
L. 84: 132     c_stmt ::= ifelsestmtc (133)
L. 84: 132     lastc_stmt ::= ifelsestmtc (133)
L. 69:  28     c_stmt ::= ifstmtc (133)
L. 66:  24     c_stmt ::= ifstmtc (133)
L. 66:  24     c_stmt ::= if_not_stmtc (133)
        24     c_suite_stmts_opt ::= suite_stmts_opt (133)
L. 89: 164     c_stmts ::= lastc_stmt (133)
L. 88: 152-240 c_stmts ::= _stmts lastc_stmt (133)
        24-240 c_stmts ::= _stmts lastc_stmt (133)
L. 66:  24-240 c_stmts ::= _stmts lastc_stmt (133)
        24-240 c_stmts ::= _stmts lastc_stmt (133)
        24-240 c_stmts ::= _stmts lastc_stmt (133)
L. 89: 164     c_stmts ::= c_stmt (133)
L. 84: 132     c_stmts ::= lastc_stmt (133)
L. 76:  72-240 c_stmts ::= _stmts lastc_stmt (133)
L. 83: 118-240 c_stmts ::= _stmts lastc_stmt (133)
L. 80:  96-240 c_stmts ::= _stmts lastc_stmt (133)
L. 78:  80-240 c_stmts ::= _stmts lastc_stmt (133)
        32-240 c_stmts ::= _stmts lastc_stmt (133)
L. 69:  28-240 c_stmts ::= _stmts lastc_stmt (133)
L. 84: 132     c_stmts ::= c_stmt (133)
L. 69:  28     c_stmts ::= c_stmt (133)
L. 66:  24     c_stmts ::= c_stmt (133)
       242-242 whileTruestmt38 ::= \e__come_froms \e_pass JUMP_LOOP (134)
Reduce whileTruestmt38 invalid by check
L. 95: 222-242 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP \e__come_froms (134)
Reduce whileTruestmt38 invalid by check
       200-242 whileTruestmt38 ::= _come_froms c_stmts JUMP_LOOP \e__come_froms (134)
Reduce whileTruestmt38 invalid by check
L. 94: 200-242 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP \e__come_froms (134)
Reduce whileTruestmt38 invalid by check
L. 89: 164-242 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP \e__come_froms (134)
Reduce whileTruestmt38 invalid by check
       152-242 whileTruestmt38 ::= _come_froms c_stmts JUMP_LOOP \e__come_froms (134)
Reduce whileTruestmt38 invalid by check
L. 88: 152-242 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP \e__come_froms (134)
Reduce whileTruestmt38 invalid by check
L. 84: 132-242 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP \e__come_froms (134)
Reduce whileTruestmt38 invalid by check
L. 83: 118-242 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP \e__come_froms (134)
Reduce whileTruestmt38 invalid by check
L. 80:  96-242 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP \e__come_froms (134)
Reduce whileTruestmt38 invalid by check
L. 78:  80-242 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP \e__come_froms (134)
Reduce whileTruestmt38 invalid by check
        72-242 whileTruestmt38 ::= _come_froms c_stmts JUMP_LOOP \e__come_froms (134)
Reduce whileTruestmt38 invalid by check
L. 76:  72-242 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP \e__come_froms (134)
Reduce whileTruestmt38 invalid by check
        72-242 whileTruestmt38 ::= _come_froms c_stmts JUMP_LOOP \e__come_froms (134)
Reduce whileTruestmt38 invalid by check
        32-242 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP \e__come_froms (134)
Reduce whileTruestmt38 invalid by check
L. 69:  28-242 whilestmt38 ::= \e__come_froms testexpr c_stmts JUMP_LOOP \e__come_froms (134)
Reduce whilestmt38 invalid by check
L. 69:  28-242 iflaststmtc ::= testexpr c_stmts JUMP_LOOP (134)
Reduce iflaststmtc invalid by check
        32-242 ifstmts_jumpc ::= c_stmts JUMP_LOOP (134)
        32-242 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP \e__come_froms (134)
Reduce whileTruestmt38 invalid by check
L. 69:  28-242 iflaststmtc ::= testexprc c_stmts JUMP_LOOP \e_opt_pop_block (134)
Reduce iflaststmtc invalid by check
        24-242 whileTruestmt38 ::= _come_froms c_stmts JUMP_LOOP \e__come_froms (134)
L. 66:  24-242 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP \e__come_froms (134)
        24-242 whileTruestmt38 ::= _come_froms c_stmts JUMP_LOOP \e__come_froms (134)
        24-242 whileTruestmt38 ::= _come_froms c_stmts JUMP_LOOP \e__come_froms (134)
        24-242 whilestmt38 ::= _come_froms testexpr c_stmts JUMP_LOOP \e__come_froms (134)
L. 69:  28-242 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP \e__come_froms (134)
Reduce whileTruestmt38 invalid by check
L. 66:  24-242 whilestmt38 ::= \e__come_froms testexpr c_stmts JUMP_LOOP \e__come_froms (134)
L. 66:  24-242 iflaststmtc ::= testexpr c_stmts JUMP_LOOP (134)
Reduce iflaststmtc invalid by check
L. 69:  28-242 ifstmts_jumpc ::= c_stmts JUMP_LOOP (134)
L. 69:  28-242 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP \e__come_froms (134)
Reduce whileTruestmt38 invalid by check
        24-242 whilestmt38 ::= _come_froms testexpr c_stmts JUMP_LOOP \e__come_froms (134)
        24-242 whilestmt38 ::= _come_froms testexpr c_stmts JUMP_LOOP \e__come_froms (134)
L. 66:  24-242 iflaststmtc ::= testexprc c_stmts JUMP_LOOP \e_opt_pop_block (134)
Reduce iflaststmtc invalid by check
        24-242 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP \e__come_froms (134)
        24-242 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP \e__come_froms (134)
        24-242 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP \e__come_froms (134)
L. 69:  28-242 ifstmtc ::= testexpr ifstmts_jumpc (134)
L. 69:  28-242 ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms (134)
Reduce ifstmtc invalid by check
L. 69:  28-242 if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms (134)
Reduce if_not_stmtc invalid by check
        24     stmt ::= whileTruestmt38 (134)
L. 66:  24     stmt ::= whileTruestmt38 (134)
        24     stmt ::= whileTruestmt38 (134)
        24     stmt ::= whileTruestmt38 (134)
        24     stmt ::= whilestmt38 (134)
L. 66:  24     stmt ::= whilestmt38 (134)
L. 66:  24-242 ifstmtc ::= testexpr ifstmts_jumpc (134)
L. 66:  24-242 ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms (134)
L. 66:  24-242 if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms (134)
Reduce if_not_stmtc invalid by check
        24     stmt ::= whilestmt38 (134)
        24     stmt ::= whilestmt38 (134)
L. 69:  28     c_stmt ::= ifstmtc (134)
        24     stmts ::= stmt (134)
        24     c_stmt ::= stmt (134)
        24     sstmt ::= stmt (134)
L. 66:  24     stmts ::= stmt (134)
L. 66:  24     c_stmt ::= stmt (134)
L. 66:  24     sstmt ::= stmt (134)
        24     stmts ::= stmt (134)
        24     c_stmt ::= stmt (134)
        24     sstmt ::= stmt (134)
        24     stmts ::= stmt (134)
        24     c_stmt ::= stmt (134)
        24     sstmt ::= stmt (134)
L. 66:  24     c_stmt ::= ifstmtc (134)
L. 69:  28     c_stmts ::= c_stmt (134)
        24     _stmts ::= stmts (134)
        24     c_stmts ::= c_stmt (134)
        24     stmts ::= sstmt (134)
L. 66:  24     _stmts ::= stmts (134)
L. 66:  24     c_stmts ::= c_stmt (134)
L. 66:  24     stmts ::= sstmt (134)
        24     _stmts ::= stmts (134)
        24     c_stmts ::= c_stmt (134)
        24     stmts ::= sstmt (134)
        24     _stmts ::= stmts (134)
        24     c_stmts ::= c_stmt (134)
        24     stmts ::= sstmt (134)
L. 69:  28     c_stmts_opt ::= c_stmts (134)
L. 66:  24-242 iflaststmtc ::= testexpr c_stmts (134)
Reduce iflaststmtc invalid by check
L. 69:  28     c_stmts_opt ::= c_stmts (134)
L. 69:  28     ifstmts_jumpc ::= c_stmts (134)
L. 66:  24-242 iflaststmtc ::= testexprc c_stmts (134)
Reduce iflaststmtc invalid by check
        24     suite_stmts ::= _stmts (134)
        24     c_stmts ::= _stmts (134)
        24     c_suite_stmts ::= c_stmts (134)
L. 66:  24     c_stmts ::= _stmts (134)
        24     c_stmts ::= _stmts (134)
        24     c_stmts ::= _stmts (134)
        24     suite_stmts_opt ::= suite_stmts (134)
        24     c_suite_stmts ::= suite_stmts (134)
        24     c_suite_stmts_opt ::= c_suite_stmts (134)
        24     c_suite_stmts_opt ::= suite_stmts_opt (134)
       244-244 _come_froms ::= \e__come_froms COME_FROM (135)
       244     come_froms ::= COME_FROM (135)
       244     come_froms ::= COME_FROM (135)
       244-244 _come_froms ::= \e__come_froms COME_FROM (135)
       244     come_froms ::= COME_FROM (135)
       244     come_from_opt ::= COME_FROM (135)
       244     come_froms ::= COME_FROM (135)
L. 95: 222-244 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP _come_froms (135)
Reduce whileTruestmt38 invalid by check
       200-244 whileTruestmt38 ::= _come_froms c_stmts JUMP_LOOP _come_froms (135)
Reduce whileTruestmt38 invalid by check
L. 94: 200-244 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP _come_froms (135)
Reduce whileTruestmt38 invalid by check
L. 89: 164-244 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP _come_froms (135)
Reduce whileTruestmt38 invalid by check
       152-244 whileTruestmt38 ::= _come_froms c_stmts JUMP_LOOP _come_froms (135)
Reduce whileTruestmt38 invalid by check
L. 88: 152-244 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP _come_froms (135)
Reduce whileTruestmt38 invalid by check
L. 84: 132-244 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP _come_froms (135)
Reduce whileTruestmt38 invalid by check
L. 83: 118-244 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP _come_froms (135)
Reduce whileTruestmt38 invalid by check
L. 80:  96-244 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP _come_froms (135)
Reduce whileTruestmt38 invalid by check
L. 78:  80-244 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP _come_froms (135)
Reduce whileTruestmt38 invalid by check
        72-244 whileTruestmt38 ::= _come_froms c_stmts JUMP_LOOP _come_froms (135)
Reduce whileTruestmt38 invalid by check
L. 76:  72-244 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP _come_froms (135)
Reduce whileTruestmt38 invalid by check
        72-244 whileTruestmt38 ::= _come_froms c_stmts JUMP_LOOP _come_froms (135)
Reduce whileTruestmt38 invalid by check
        32-244 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP _come_froms (135)
Reduce whileTruestmt38 invalid by check
L. 69:  28-244 whilestmt38 ::= \e__come_froms testexpr c_stmts JUMP_LOOP _come_froms (135)
Reduce whilestmt38 invalid by check
        24-244 whileTruestmt38 ::= _come_froms c_stmts JUMP_LOOP _come_froms (135)
L. 66:  24-244 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP _come_froms (135)
        24-244 whileTruestmt38 ::= _come_froms c_stmts JUMP_LOOP _come_froms (135)
        24-244 whileTruestmt38 ::= _come_froms c_stmts JUMP_LOOP _come_froms (135)
        24-244 whilestmt38 ::= _come_froms testexpr c_stmts JUMP_LOOP _come_froms (135)
L. 69:  28-244 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP _come_froms (135)
Reduce whileTruestmt38 invalid by check
L. 66:  24-244 whilestmt38 ::= \e__come_froms testexpr c_stmts JUMP_LOOP _come_froms (135)
        24-244 whilestmt38 ::= _come_froms testexpr c_stmts JUMP_LOOP _come_froms (135)
        24-244 whilestmt38 ::= _come_froms testexpr c_stmts JUMP_LOOP _come_froms (135)
        24-244 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP _come_froms (135)
        24-244 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP _come_froms (135)
        24-244 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP _come_froms (135)
L. 69:  28-244 ifstmtc ::= testexprc ifstmts_jumpc _come_froms (135)
Reduce ifstmtc invalid by check
L. 69:  28-244 if_not_stmtc ::= testexprc ifstmts_jumpc _come_froms (135)
Reduce if_not_stmtc invalid by check
L. 66:  24-244 ifstmtc ::= testexprc ifstmts_jumpc _come_froms (135)
L. 66:  24-244 if_not_stmtc ::= testexprc ifstmts_jumpc _come_froms (135)
Reduce if_not_stmtc invalid by check
       242-244 jb_cfs ::= \e_come_from_opt JUMP_LOOP come_froms (135)
L. 89: 164-244 ifelsestmtc ::= testexpr c_stmts_opt jb_cfs else_suitec JUMP_LOOP come_froms (135)
L. 69:  28-244 ifelsestmtc ::= testexpr c_stmts_opt jb_cfs else_suitec JUMP_LOOP come_froms (135)
Reduce ifelsestmtc invalid by check
L. 66:  24-244 ifelsestmtc ::= testexpr c_stmts_opt jb_cfs else_suitec JUMP_LOOP come_froms (135)
Reduce ifelsestmtc invalid by check
L. 84: 132-244 ifelsestmtc ::= testexpr c_stmts_opt jb_cfs else_suitec JUMP_LOOP come_froms (135)
L. 69:  28-244 whilestmt38 ::= \e__come_froms testexpr c_stmts_opt JUMP_LOOP come_froms (135)
Reduce whilestmt38 invalid by check
        24-244 whilestmt38 ::= _come_froms testexpr c_stmts_opt JUMP_LOOP come_froms (135)
L. 66:  24-244 whilestmt38 ::= \e__come_froms testexpr c_stmts_opt JUMP_LOOP come_froms (135)
        24-244 whilestmt38 ::= _come_froms testexpr c_stmts_opt JUMP_LOOP come_froms (135)
        24-244 whilestmt38 ::= _come_froms testexpr c_stmts_opt JUMP_LOOP come_froms (135)
        24-244 whilestmt38 ::= _come_froms testexpr c_stmts come_froms (135)
L. 66:  24-244 whilestmt38 ::= \e__come_froms testexpr c_stmts come_froms (135)
L. 66:  24-244 iflaststmtc ::= testexpr c_stmts come_froms (135)
Reduce iflaststmtc invalid by check
        24-244 whilestmt38 ::= _come_froms testexpr c_stmts come_froms (135)
        24-244 whilestmt38 ::= _come_froms testexpr c_stmts come_froms (135)
L. 69:  28-244 ifstmts_jumpc ::= c_stmts_opt come_froms (135)
        24     stmt ::= whileTruestmt38 (135)
L. 66:  24     stmt ::= whileTruestmt38 (135)
        24     stmt ::= whileTruestmt38 (135)
        24     stmt ::= whileTruestmt38 (135)
        24     stmt ::= whilestmt38 (135)
L. 66:  24     stmt ::= whilestmt38 (135)
        24     stmt ::= whilestmt38 (135)
        24     stmt ::= whilestmt38 (135)
L. 66:  24     c_stmt ::= ifstmtc (135)
L. 89: 164     lastc_stmt ::= ifelsestmtc (135)
Reduce lastc_stmt invalid by check
L. 89: 164     c_stmt ::= ifelsestmtc (135)
L. 89: 164     lastc_stmt ::= ifelsestmtc (135)
Reduce lastc_stmt invalid by check
L. 84: 132     lastc_stmt ::= ifelsestmtc (135)
Reduce lastc_stmt invalid by check
L. 84: 132     c_stmt ::= ifelsestmtc (135)
L. 84: 132     lastc_stmt ::= ifelsestmtc (135)
Reduce lastc_stmt invalid by check
L. 66:  24-244 ifstmtc ::= testexpr ifstmts_jumpc (135)
L. 66:  24-244 ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms (135)
L. 66:  24-244 if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms (135)
Reduce if_not_stmtc invalid by check
        24     stmts ::= stmt (135)
        24     c_stmt ::= stmt (135)
        24     sstmt ::= stmt (135)
L. 66:  24     stmts ::= stmt (135)
L. 66:  24     c_stmt ::= stmt (135)
L. 66:  24     sstmt ::= stmt (135)
        24     stmts ::= stmt (135)
        24     c_stmt ::= stmt (135)
        24     sstmt ::= stmt (135)
        24     stmts ::= stmt (135)
        24     c_stmt ::= stmt (135)
        24     sstmt ::= stmt (135)
L. 66:  24     c_stmts ::= c_stmt (135)
L. 89: 164     c_stmts ::= c_stmt (135)
L. 88: 152-244 c_stmts ::= c_stmts c_stmt (135)
L. 84: 132-244 c_stmts ::= c_stmts c_stmt (135)
L. 83: 118-244 c_stmts ::= c_stmts c_stmt (135)
L. 80:  96-244 c_stmts ::= c_stmts c_stmt (135)
L. 78:  80-244 c_stmts ::= c_stmts c_stmt (135)
L. 76:  72-244 c_stmts ::= c_stmts c_stmt (135)
        32-244 c_stmts ::= c_stmts c_stmt (135)
L. 66:  24-244 c_stmts ::= c_stmts c_stmt (135)
L. 69:  28-244 c_stmts ::= c_stmts c_stmt (135)
        24-244 c_stmts ::= c_stmts c_stmt (135)
        24-244 c_stmts ::= c_stmts c_stmt (135)
        24-244 c_stmts ::= c_stmts c_stmt (135)
L. 84: 132     c_stmts ::= c_stmt (135)
        24     _stmts ::= stmts (135)
        24     c_stmts ::= c_stmt (135)
        24     stmts ::= sstmt (135)
L. 66:  24     _stmts ::= stmts (135)
L. 66:  24     stmts ::= sstmt (135)
        24     _stmts ::= stmts (135)
        24     c_stmts ::= c_stmt (135)
        24     stmts ::= sstmt (135)
        24     _stmts ::= stmts (135)
        24     c_stmts ::= c_stmt (135)
        24     stmts ::= sstmt (135)
L. 88: 152     else_suitec ::= c_stmts (135)
L. 69:  28-244 iflaststmtc ::= testexpr c_stmts (135)
Reduce iflaststmtc invalid by check
        32     c_stmts_opt ::= c_stmts (135)
        32     ifstmts_jumpc ::= c_stmts (135)
L. 69:  28-244 iflaststmtc ::= testexprc c_stmts (135)
Reduce iflaststmtc invalid by check
L. 69:  28     c_stmts_opt ::= c_stmts (135)
L. 66:  24-244 iflaststmtc ::= testexpr c_stmts (135)
Reduce iflaststmtc invalid by check
L. 69:  28     c_stmts_opt ::= c_stmts (135)
L. 69:  28     ifstmts_jumpc ::= c_stmts (135)
L. 66:  24-244 iflaststmtc ::= testexprc c_stmts (135)
Reduce iflaststmtc invalid by check
        24     c_suite_stmts ::= c_stmts (135)
        24     suite_stmts ::= _stmts (135)
        24     c_stmts ::= _stmts (135)
L. 66:  24     c_stmts ::= _stmts (135)
        24     c_stmts ::= _stmts (135)
        24     c_stmts ::= _stmts (135)
L. 84: 132-244 ifelsestmtc ::= testexpr c_stmts_opt jb_cfs else_suitec (135)
L. 66:  24-244 if_and_elsestmtc ::= expr_pjif expr_pjif c_stmts jb_cfs else_suitec \e_opt_come_from_except (135)
Reduce if_and_elsestmtc invalid by check
L. 69:  28-244 ifelsestmtc ::= testexpr c_stmts_opt jb_cfs else_suitec (135)
Reduce ifelsestmtc invalid by check
L. 66:  24-244 ifelsestmtc ::= testexpr c_stmts_opt jb_cfs else_suitec (135)
Reduce ifelsestmtc invalid by check
L. 69:  28-244 ifstmtc ::= testexpr ifstmts_jumpc (135)
Reduce ifstmtc invalid by check
L. 69:  28-244 ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms (135)
Reduce ifstmtc invalid by check
L. 69:  28-244 if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms (135)
Reduce if_not_stmtc invalid by check
        24     c_suite_stmts_opt ::= c_suite_stmts (135)
        24     suite_stmts_opt ::= suite_stmts (135)
        24     c_suite_stmts ::= suite_stmts (135)
        24     c_suite_stmts_opt ::= suite_stmts_opt (135)
       244-244 _come_froms ::= _come_froms COME_FROM (136)
       244-244 _come_froms ::= \e__come_froms COME_FROM (136)
       244-244 come_froms ::= come_froms COME_FROM (136)
       244     come_from_opt ::= COME_FROM (136)
       244     come_froms ::= COME_FROM (136)
       244     come_froms ::= COME_FROM (136)
       244     come_any_from ::= COME_FROM (136)
       244     come_from_opt ::= COME_FROM (136)
       244     come_froms ::= COME_FROM (136)
L. 95: 222-244 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP _come_froms (136)
Reduce whileTruestmt38 invalid by check
       200-244 whileTruestmt38 ::= _come_froms c_stmts JUMP_LOOP _come_froms (136)
Reduce whileTruestmt38 invalid by check
L. 94: 200-244 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP _come_froms (136)
Reduce whileTruestmt38 invalid by check
L. 89: 164-244 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP _come_froms (136)
Reduce whileTruestmt38 invalid by check
       152-244 whileTruestmt38 ::= _come_froms c_stmts JUMP_LOOP _come_froms (136)
Reduce whileTruestmt38 invalid by check
L. 88: 152-244 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP _come_froms (136)
Reduce whileTruestmt38 invalid by check
L. 84: 132-244 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP _come_froms (136)
Reduce whileTruestmt38 invalid by check
L. 83: 118-244 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP _come_froms (136)
Reduce whileTruestmt38 invalid by check
L. 80:  96-244 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP _come_froms (136)
Reduce whileTruestmt38 invalid by check
L. 78:  80-244 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP _come_froms (136)
Reduce whileTruestmt38 invalid by check
        72-244 whileTruestmt38 ::= _come_froms c_stmts JUMP_LOOP _come_froms (136)
Reduce whileTruestmt38 invalid by check
L. 76:  72-244 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP _come_froms (136)
Reduce whileTruestmt38 invalid by check
        72-244 whileTruestmt38 ::= _come_froms c_stmts JUMP_LOOP _come_froms (136)
Reduce whileTruestmt38 invalid by check
        32-244 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP _come_froms (136)
Reduce whileTruestmt38 invalid by check
L. 69:  28-244 whilestmt38 ::= \e__come_froms testexpr c_stmts JUMP_LOOP _come_froms (136)
Reduce whilestmt38 invalid by check
        24-244 whileTruestmt38 ::= _come_froms c_stmts JUMP_LOOP _come_froms (136)
L. 66:  24-244 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP _come_froms (136)
        24-244 whileTruestmt38 ::= _come_froms c_stmts JUMP_LOOP _come_froms (136)
        24-244 whileTruestmt38 ::= _come_froms c_stmts JUMP_LOOP _come_froms (136)
        24-244 whilestmt38 ::= _come_froms testexpr c_stmts JUMP_LOOP _come_froms (136)
L. 69:  28-244 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP _come_froms (136)
Reduce whileTruestmt38 invalid by check
L. 66:  24-244 whilestmt38 ::= \e__come_froms testexpr c_stmts JUMP_LOOP _come_froms (136)
        24-244 whilestmt38 ::= _come_froms testexpr c_stmts JUMP_LOOP _come_froms (136)
        24-244 whilestmt38 ::= _come_froms testexpr c_stmts JUMP_LOOP _come_froms (136)
        24-244 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP _come_froms (136)
        24-244 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP _come_froms (136)
        24-244 whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP _come_froms (136)
L. 69:  28-244 ifstmtc ::= testexprc ifstmts_jumpc _come_froms (136)
L. 69:  28-244 if_not_stmtc ::= testexprc ifstmts_jumpc _come_froms (136)
Reduce if_not_stmtc invalid by check
L. 66:  24-244 ifstmtc ::= testexprc ifstmts_jumpc _come_froms (136)
L. 66:  24-244 if_not_stmtc ::= testexprc ifstmts_jumpc _come_froms (136)
Reduce if_not_stmtc invalid by check
       242-244 jb_cfs ::= \e_come_from_opt JUMP_LOOP come_froms (136)
L. 89: 164-244 ifelsestmtc ::= testexpr c_stmts_opt jb_cfs else_suitec JUMP_LOOP come_froms (136)
Reduce ifelsestmtc invalid by check
L. 69:  28-244 ifelsestmtc ::= testexpr c_stmts_opt jb_cfs else_suitec JUMP_LOOP come_froms (136)
Reduce ifelsestmtc invalid by check
L. 66:  24-244 ifelsestmtc ::= testexpr c_stmts_opt jb_cfs else_suitec JUMP_LOOP come_froms (136)
Reduce ifelsestmtc invalid by check
L. 84: 132-244 ifelsestmtc ::= testexpr c_stmts_opt jb_cfs else_suitec JUMP_LOOP come_froms (136)
Reduce ifelsestmtc invalid by check
L. 69:  28-244 whilestmt38 ::= \e__come_froms testexpr c_stmts_opt JUMP_LOOP come_froms (136)
Reduce whilestmt38 invalid by check
        24-244 whilestmt38 ::= _come_froms testexpr c_stmts_opt JUMP_LOOP come_froms (136)
L. 66:  24-244 whilestmt38 ::= \e__come_froms testexpr c_stmts_opt JUMP_LOOP come_froms (136)
        24-244 whilestmt38 ::= _come_froms testexpr c_stmts_opt JUMP_LOOP come_froms (136)
        24-244 whilestmt38 ::= _come_froms testexpr c_stmts_opt JUMP_LOOP come_froms (136)
        24-244 whilestmt38 ::= _come_froms testexpr c_stmts come_froms (136)
L. 66:  24-244 whilestmt38 ::= \e__come_froms testexpr c_stmts come_froms (136)
L. 66:  24-244 iflaststmtc ::= testexpr c_stmts come_froms (136)
Reduce iflaststmtc invalid by check
        24-244 whilestmt38 ::= _come_froms testexpr c_stmts come_froms (136)
        24-244 whilestmt38 ::= _come_froms testexpr c_stmts come_froms (136)
L. 69:  28-244 ifstmts_jumpc ::= c_stmts_opt come_froms (136)
L. 69:  28-244 whilestmt38 ::= \e__come_froms testexpr c_stmts come_froms (136)
Reduce whilestmt38 invalid by check
L. 69:  28-244 iflaststmtc ::= testexpr c_stmts come_froms (136)
Reduce iflaststmtc invalid by check
        32-244 ifstmts_jumpc ::= c_stmts_opt come_froms (136)
       244     come_any_froms ::= come_any_from (136)
        24     stmt ::= whileTruestmt38 (136)
L. 66:  24     stmt ::= whileTruestmt38 (136)
        24     stmt ::= whileTruestmt38 (136)
        24     stmt ::= whileTruestmt38 (136)
        24     stmt ::= whilestmt38 (136)
L. 66:  24     stmt ::= whilestmt38 (136)
        24     stmt ::= whilestmt38 (136)
        24     stmt ::= whilestmt38 (136)
L. 69:  28     c_stmt ::= ifstmtc (136)
L. 66:  24     c_stmt ::= ifstmtc (136)
L. 66:  24-244 ifstmtc ::= testexpr ifstmts_jumpc (136)
L. 66:  24-244 ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms (136)
L. 66:  24-244 if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms (136)
Reduce if_not_stmtc invalid by check
L. 69:  28-244 ifstmtc ::= testexpr ifstmts_jumpc (136)
L. 69:  28-244 ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms (136)
Reduce ifstmtc invalid by check
L. 69:  28-244 if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms (136)
Reduce if_not_stmtc invalid by check
       244     opt_come_from_except ::= come_any_froms (136)
        24     stmts ::= stmt (136)
        24     c_stmt ::= stmt (136)
        24     sstmt ::= stmt (136)
L. 66:  24     stmts ::= stmt (136)
L. 66:  24     c_stmt ::= stmt (136)
L. 66:  24     sstmt ::= stmt (136)
        24     stmts ::= stmt (136)
        24     c_stmt ::= stmt (136)
        24     sstmt ::= stmt (136)
        24     stmts ::= stmt (136)
        24     c_stmt ::= stmt (136)
        24     sstmt ::= stmt (136)
L. 69:  28     c_stmts ::= c_stmt (136)
L. 66:  24     c_stmts ::= c_stmt (136)
L. 66:  24-244 if_and_elsestmtc ::= expr_pjif expr_pjif c_stmts jb_cfs else_suitec opt_come_from_except (136)
Reduce if_and_elsestmtc invalid by check
        24     _stmts ::= stmts (136)
        24     c_stmts ::= c_stmt (136)
        24     stmts ::= sstmt (136)
L. 66:  24     _stmts ::= stmts (136)
L. 66:  24     stmts ::= sstmt (136)
        24     _stmts ::= stmts (136)
        24     c_stmts ::= c_stmt (136)
        24     stmts ::= sstmt (136)
        24     _stmts ::= stmts (136)
        24     c_stmts ::= c_stmt (136)
        24     stmts ::= sstmt (136)
L. 69:  28     c_stmts_opt ::= c_stmts (136)
L. 66:  24-244 iflaststmtc ::= testexpr c_stmts (136)
Reduce iflaststmtc invalid by check
L. 69:  28     c_stmts_opt ::= c_stmts (136)
L. 69:  28     ifstmts_jumpc ::= c_stmts (136)
L. 66:  24-244 iflaststmtc ::= testexprc c_stmts (136)
Reduce iflaststmtc invalid by check
        24     suite_stmts ::= _stmts (136)
        24     c_stmts ::= _stmts (136)
        24     c_suite_stmts ::= c_stmts (136)
L. 66:  24     c_stmts ::= _stmts (136)
        24     c_stmts ::= _stmts (136)
        24     c_stmts ::= _stmts (136)
        24     suite_stmts_opt ::= suite_stmts (136)
        24     c_suite_stmts ::= suite_stmts (136)
        24     c_suite_stmts_opt ::= c_suite_stmts (136)
        24     c_suite_stmts_opt ::= suite_stmts_opt (136)
L. 97: 244     expr ::= LOAD_FAST (137)
L. 97: 244     return_expr ::= expr (137)
L. 97: 244     return_expr ::= expr (137)
L. 97: 244     return_expr ::= expr (137)
L. 97: 244-246 expr_pjif ::= expr POP_JUMP_IF_FALSE (138)
L. 97: 244-246 expr_pjif ::= expr POP_JUMP_IF_FALSE (138)
L. 97: 244     testfalse ::= expr_pjif (138)
L. 97: 244     and_parts ::= expr_pjif (138)
L. 97: 244     and_parts ::= expr_pjif (138)
L. 97: 244     testfalse ::= expr_pjif (138)
L. 97: 244     testexpr ::= testfalse (138)
L. 97: 244     testexprc ::= testexpr (138)
L. 97: 244     testexprc ::= testexpr (138)

-- Stacks of completed symbols:
START ::= |- stmts . 
_come_froms ::= \e__come_froms . COME_FROM
_come_froms ::= \e__come_froms COME_FROM . 
_come_froms ::= _come_froms . COME_FROM
_come_froms ::= _come_froms COME_FROM . 
_stmts ::= stmts . 
and_cond ::= and_parts . expr_pjif \e__come_froms
and_cond ::= and_parts . expr_pjif _come_froms
and_cond ::= and_parts expr_pjif . _come_froms
and_cond ::= and_parts expr_pjif \e__come_froms . 
and_cond ::= testfalse . expr_pjif \e__come_froms
and_cond ::= testfalse . expr_pjif _come_froms
and_cond ::= testfalse expr_pjif . _come_froms
and_cond ::= testfalse expr_pjif \e__come_froms . 
and_not ::= expr_pjif . expr_pjit
and_or_cond ::= and_parts . expr POP_JUMP_IF_TRUE come_froms expr_pjif \e__come_froms
and_or_cond ::= and_parts . expr POP_JUMP_IF_TRUE come_froms expr_pjif _come_froms
and_or_cond ::= and_parts expr . POP_JUMP_IF_TRUE come_froms expr_pjif \e__come_froms
and_or_cond ::= and_parts expr . POP_JUMP_IF_TRUE come_froms expr_pjif _come_froms
and_or_expr ::= and_parts . expr jitop_come_from_expr COME_FROM
and_or_expr ::= and_parts expr . jitop_come_from_expr COME_FROM
and_parts ::= and_parts . expr_pjif
and_parts ::= and_parts expr_pjif . 
and_parts ::= expr_pjif . 
assert2 ::= expr . POP_JUMP_IF_TRUE LOAD_GLOBAL expr CALL_FUNCTION_1 RAISE_VARARGS_1
assert2 ::= expr POP_JUMP_IF_TRUE . LOAD_GLOBAL expr CALL_FUNCTION_1 RAISE_VARARGS_1
assert2_not ::= expr . POP_JUMP_IF_FALSE LOAD_GLOBAL expr CALL_FUNCTION_1 RAISE_VARARGS_1
assert2_not ::= expr POP_JUMP_IF_FALSE . LOAD_GLOBAL expr CALL_FUNCTION_1 RAISE_VARARGS_1
assert2_not ::= expr POP_JUMP_IF_FALSE LOAD_GLOBAL . expr CALL_FUNCTION_1 RAISE_VARARGS_1
assert_invert ::= testtrue . LOAD_GLOBAL RAISE_VARARGS_1
assign ::= expr . DUP_TOP designList
assign ::= expr . store
assign ::= expr store . 
assign2 ::= expr . expr ROT_TWO store store
assign2 ::= expr expr . ROT_TWO store store
assign3 ::= expr . expr expr ROT_THREE ROT_TWO store store store
assign3 ::= expr expr . expr ROT_THREE ROT_TWO store store store
assign3 ::= expr expr expr . ROT_THREE ROT_TWO store store store
async_with_stmt38 ::= expr . BEFORE_ASYNC_WITH GET_AWAITABLE LOAD_CONST YIELD_FROM SETUP_ASYNC_WITH POP_TOP \e_c_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM_ASYNC_WITH WITH_CLEANUP_START GET_AWAITABLE LOAD_CONST YIELD_FROM WITH_CLEANUP_FINISH END_FINALLY
async_with_stmt38 ::= expr . BEFORE_ASYNC_WITH GET_AWAITABLE LOAD_CONST YIELD_FROM SETUP_ASYNC_WITH POP_TOP \e_c_stmts_opt POP_BLOCK BEGIN_FINALLY WITH_CLEANUP_START GET_AWAITABLE LOAD_CONST YIELD_FROM WITH_CLEANUP_FINISH POP_FINALLY
async_with_stmt38 ::= expr . BEFORE_ASYNC_WITH GET_AWAITABLE LOAD_CONST YIELD_FROM SETUP_ASYNC_WITH POP_TOP \e_c_stmts_opt POP_BLOCK BEGIN_FINALLY WITH_CLEANUP_START GET_AWAITABLE LOAD_CONST YIELD_FROM WITH_CLEANUP_FINISH POP_FINALLY JUMP_LOOP
async_with_stmt38 ::= expr . BEFORE_ASYNC_WITH GET_AWAITABLE LOAD_CONST YIELD_FROM SETUP_ASYNC_WITH POP_TOP c_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM_ASYNC_WITH WITH_CLEANUP_START GET_AWAITABLE LOAD_CONST YIELD_FROM WITH_CLEANUP_FINISH END_FINALLY
async_with_stmt38 ::= expr . BEFORE_ASYNC_WITH GET_AWAITABLE LOAD_CONST YIELD_FROM SETUP_ASYNC_WITH POP_TOP c_stmts_opt POP_BLOCK BEGIN_FINALLY WITH_CLEANUP_START GET_AWAITABLE LOAD_CONST YIELD_FROM WITH_CLEANUP_FINISH POP_FINALLY
async_with_stmt38 ::= expr . BEFORE_ASYNC_WITH GET_AWAITABLE LOAD_CONST YIELD_FROM SETUP_ASYNC_WITH POP_TOP c_stmts_opt POP_BLOCK BEGIN_FINALLY WITH_CLEANUP_START GET_AWAITABLE LOAD_CONST YIELD_FROM WITH_CLEANUP_FINISH POP_FINALLY JUMP_LOOP
attribute ::= expr . LOAD_ATTR
attribute ::= expr LOAD_ATTR . 
attribute37 ::= expr . LOAD_METHOD
attribute37 ::= expr LOAD_METHOD . 
aug_assign1 ::= expr . expr inplace_op ROT_THREE STORE_SUBSCR
aug_assign1 ::= expr . expr inplace_op store
aug_assign1 ::= expr expr . inplace_op ROT_THREE STORE_SUBSCR
aug_assign1 ::= expr expr . inplace_op store
aug_assign1 ::= expr expr inplace_op . ROT_THREE STORE_SUBSCR
aug_assign1 ::= expr expr inplace_op . store
aug_assign1 ::= expr expr inplace_op store . 
aug_assign2 ::= expr . DUP_TOP LOAD_ATTR expr inplace_op ROT_TWO STORE_ATTR
await_expr ::= expr . GET_AWAITABLE LOAD_CONST YIELD_FROM
bin_op ::= expr . expr binary_operator
bin_op ::= expr expr . binary_operator
bin_op ::= expr expr binary_operator . 
binary_operator ::= BINARY_ADD . 
binary_operator ::= BINARY_AND . 
binary_operator ::= BINARY_MODULO . 
bool_op ::= and_cond . 
break ::= BREAK_LOOP . 
break ::= POP_BLOCK . BREAK_LOOP
break ::= POP_BLOCK . POP_TOP BREAK_LOOP
break ::= POP_BLOCK . POP_TOP JUMP_FORWARD
c_compare_chained37 ::= expr . c_compare_chained_middlea_37
c_compare_chained37_false ::= expr . c_compare_chained_middleb_false_37
c_compare_chained37_false ::= expr . c_compare_chained_right_false_37
c_forelsestmt38 ::= expr . get_for_iter store for_block JUMP_LOOP \e__come_froms else_suitec
c_forelsestmt38 ::= expr . get_for_iter store for_block JUMP_LOOP _come_froms else_suitec
c_forelsestmt38 ::= expr . get_for_iter store for_block POP_BLOCK else_suitec
c_nand ::= and_parts . expr_pjitt come_froms
c_returns ::= c_stmts . return
c_returns ::= returns . 
c_stmt ::= break . 
c_stmt ::= if_not_stmtc . 
c_stmt ::= ifelsestmtc . 
c_stmt ::= ifstmtc . 
c_stmt ::= stmt . 
c_stmts ::= _stmts . 
c_stmts ::= _stmts . lastc_stmt
c_stmts ::= _stmts lastc_stmt . 
c_stmts ::= c_returns . 
c_stmts ::= c_stmt . 
c_stmts ::= c_stmts . c_stmt
c_stmts ::= c_stmts c_stmt . 
c_stmts ::= lastc_stmt . 
c_stmts_opt ::= c_stmts . 
c_suite_stmts ::= c_stmts . 
c_suite_stmts ::= suite_stmts . 
c_suite_stmts_opt ::= c_suite_stmts . 
c_suite_stmts_opt ::= suite_stmts_opt . 
c_try_except ::= SETUP_FINALLY . c_suite_stmts POP_BLOCK except_handler38
c_try_except ::= SETUP_FINALLY c_suite_stmts . POP_BLOCK except_handler38
c_tryfinallybstmt38 ::= SETUP_FINALLY . c_suite_stmts_opt POP_BLOCK CALL_FINALLY POP_BLOCK POP_EXCEPT CALL_FINALLY BREAK_LOOP POP_BLOCK BEGIN_FINALLY COME_FROM COME_FROM_FINALLY \e_c_suite_stmts_opt END_FINALLY
c_tryfinallybstmt38 ::= SETUP_FINALLY . c_suite_stmts_opt POP_BLOCK CALL_FINALLY POP_BLOCK POP_EXCEPT CALL_FINALLY BREAK_LOOP POP_BLOCK BEGIN_FINALLY COME_FROM COME_FROM_FINALLY c_suite_stmts_opt END_FINALLY
c_tryfinallybstmt38 ::= SETUP_FINALLY \e_c_suite_stmts_opt . POP_BLOCK CALL_FINALLY POP_BLOCK POP_EXCEPT CALL_FINALLY BREAK_LOOP POP_BLOCK BEGIN_FINALLY COME_FROM COME_FROM_FINALLY \e_c_suite_stmts_opt END_FINALLY
c_tryfinallybstmt38 ::= SETUP_FINALLY \e_c_suite_stmts_opt . POP_BLOCK CALL_FINALLY POP_BLOCK POP_EXCEPT CALL_FINALLY BREAK_LOOP POP_BLOCK BEGIN_FINALLY COME_FROM COME_FROM_FINALLY c_suite_stmts_opt END_FINALLY
c_tryfinallybstmt38 ::= SETUP_FINALLY c_suite_stmts_opt . POP_BLOCK CALL_FINALLY POP_BLOCK POP_EXCEPT CALL_FINALLY BREAK_LOOP POP_BLOCK BEGIN_FINALLY COME_FROM COME_FROM_FINALLY \e_c_suite_stmts_opt END_FINALLY
c_tryfinallybstmt38 ::= SETUP_FINALLY c_suite_stmts_opt . POP_BLOCK CALL_FINALLY POP_BLOCK POP_EXCEPT CALL_FINALLY BREAK_LOOP POP_BLOCK BEGIN_FINALLY COME_FROM COME_FROM_FINALLY c_suite_stmts_opt END_FINALLY
c_tryfinallystmt ::= SETUP_FINALLY . c_suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_FINALLY \e_c_suite_stmts_opt END_FINALLY
c_tryfinallystmt ::= SETUP_FINALLY . c_suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_FINALLY c_suite_stmts_opt END_FINALLY
c_tryfinallystmt ::= SETUP_FINALLY \e_c_suite_stmts_opt . POP_BLOCK LOAD_CONST COME_FROM_FINALLY \e_c_suite_stmts_opt END_FINALLY
c_tryfinallystmt ::= SETUP_FINALLY \e_c_suite_stmts_opt . POP_BLOCK LOAD_CONST COME_FROM_FINALLY c_suite_stmts_opt END_FINALLY
c_tryfinallystmt ::= SETUP_FINALLY c_suite_stmts_opt . POP_BLOCK LOAD_CONST COME_FROM_FINALLY \e_c_suite_stmts_opt END_FINALLY
c_tryfinallystmt ::= SETUP_FINALLY c_suite_stmts_opt . POP_BLOCK LOAD_CONST COME_FROM_FINALLY c_suite_stmts_opt END_FINALLY
c_tryfinallystmt38 ::= SETUP_FINALLY . c_suite_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM COME_FROM_FINALLY \e_c_suite_stmts_opt END_FINALLY
c_tryfinallystmt38 ::= SETUP_FINALLY . c_suite_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM COME_FROM_FINALLY c_suite_stmts_opt END_FINALLY
c_tryfinallystmt38 ::= SETUP_FINALLY . c_suite_stmts_opt POP_BLOCK CALL_FINALLY POP_BLOCK POP_EXCEPT CALL_FINALLY JUMP_FORWARD POP_BLOCK BEGIN_FINALLY COME_FROM COME_FROM_FINALLY \e_c_suite_stmts_opt END_FINALLY
c_tryfinallystmt38 ::= SETUP_FINALLY . c_suite_stmts_opt POP_BLOCK CALL_FINALLY POP_BLOCK POP_EXCEPT CALL_FINALLY JUMP_FORWARD POP_BLOCK BEGIN_FINALLY COME_FROM COME_FROM_FINALLY c_suite_stmts_opt END_FINALLY
c_tryfinallystmt38 ::= SETUP_FINALLY \e_c_suite_stmts_opt . POP_BLOCK BEGIN_FINALLY COME_FROM COME_FROM_FINALLY \e_c_suite_stmts_opt END_FINALLY
c_tryfinallystmt38 ::= SETUP_FINALLY \e_c_suite_stmts_opt . POP_BLOCK BEGIN_FINALLY COME_FROM COME_FROM_FINALLY c_suite_stmts_opt END_FINALLY
c_tryfinallystmt38 ::= SETUP_FINALLY \e_c_suite_stmts_opt . POP_BLOCK CALL_FINALLY POP_BLOCK POP_EXCEPT CALL_FINALLY JUMP_FORWARD POP_BLOCK BEGIN_FINALLY COME_FROM COME_FROM_FINALLY \e_c_suite_stmts_opt END_FINALLY
c_tryfinallystmt38 ::= SETUP_FINALLY \e_c_suite_stmts_opt . POP_BLOCK CALL_FINALLY POP_BLOCK POP_EXCEPT CALL_FINALLY JUMP_FORWARD POP_BLOCK BEGIN_FINALLY COME_FROM COME_FROM_FINALLY c_suite_stmts_opt END_FINALLY
c_tryfinallystmt38 ::= SETUP_FINALLY c_suite_stmts_opt . POP_BLOCK BEGIN_FINALLY COME_FROM COME_FROM_FINALLY \e_c_suite_stmts_opt END_FINALLY
c_tryfinallystmt38 ::= SETUP_FINALLY c_suite_stmts_opt . POP_BLOCK BEGIN_FINALLY COME_FROM COME_FROM_FINALLY c_suite_stmts_opt END_FINALLY
c_tryfinallystmt38 ::= SETUP_FINALLY c_suite_stmts_opt . POP_BLOCK CALL_FINALLY POP_BLOCK POP_EXCEPT CALL_FINALLY JUMP_FORWARD POP_BLOCK BEGIN_FINALLY COME_FROM COME_FROM_FINALLY \e_c_suite_stmts_opt END_FINALLY
c_tryfinallystmt38 ::= SETUP_FINALLY c_suite_stmts_opt . POP_BLOCK CALL_FINALLY POP_BLOCK POP_EXCEPT CALL_FINALLY JUMP_FORWARD POP_BLOCK BEGIN_FINALLY COME_FROM COME_FROM_FINALLY c_suite_stmts_opt END_FINALLY
call ::= expr . CALL_METHOD_0
call ::= expr . expr CALL_FUNCTION_1
call ::= expr . expr CALL_METHOD_1
call ::= expr . expr expr CALL_FUNCTION_2
call ::= expr . expr expr CALL_METHOD_2
call ::= expr CALL_METHOD_0 . 
call ::= expr expr . CALL_FUNCTION_1
call ::= expr expr . CALL_METHOD_1
call ::= expr expr . expr CALL_FUNCTION_2
call ::= expr expr . expr CALL_METHOD_2
call ::= expr expr CALL_FUNCTION_1 . 
call ::= expr expr CALL_METHOD_1 . 
call ::= expr expr expr . CALL_FUNCTION_2
call ::= expr expr expr . CALL_METHOD_2
call ::= expr expr expr CALL_METHOD_2 . 
call_kw36 ::= expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_3
cf_jump_back ::= COME_FROM . JUMP_LOOP
cf_pt ::= COME_FROM . POP_TOP
chained_part ::= expr . DUP_TOP ROT_THREE COMPARE_OP \e_come_from_opt POP_JUMP_IF_FALSE
chained_part ::= expr . DUP_TOP ROT_THREE COMPARE_OP \e_come_from_opt POP_JUMP_IF_FALSE_LOOP
chained_part ::= expr . DUP_TOP ROT_THREE COMPARE_OP come_from_opt POP_JUMP_IF_FALSE
chained_part ::= expr . DUP_TOP ROT_THREE COMPARE_OP come_from_opt POP_JUMP_IF_FALSE_LOOP
classdefdeco1 ::= expr . classdefdeco1 CALL_FUNCTION_1
classdefdeco1 ::= expr . classdefdeco2 CALL_FUNCTION_1
come_any_from ::= COME_FROM . 
come_any_froms ::= come_any_from . 
come_any_froms ::= come_any_froms . come_any_from
come_from_opt ::= COME_FROM . 
come_froms ::= COME_FROM . 
come_froms ::= come_froms . COME_FROM
come_froms ::= come_froms COME_FROM . 
compare ::= compare_single . 
compare_chained ::= expr . compare_chained_middle ROT_TWO POP_TOP \e__come_froms
compare_chained ::= expr . compare_chained_middle ROT_TWO POP_TOP _come_froms
compare_chained37 ::= expr . chained_parts
compare_chained37 ::= expr . compare_chained_middlea_37
compare_chained37 ::= expr . compare_chained_middlec_37
compare_chained37_false ::= expr . compare_chained_middle_false_37
compare_chained37_false ::= expr . compare_chained_middleb_false_37
compare_chained37_false ::= expr . compare_chained_right_false_37
compare_chained_and ::= expr . chained_parts compare_chained_righta_false_37 come_froms POP_TOP JUMP_FORWARD COME_FROM negated_testtrue come_froms
compare_chained_middle ::= expr . DUP_TOP ROT_THREE COMPARE_OP JUMP_IF_FALSE_OR_POP compare_chained_middle COME_FROM
compare_chained_middle ::= expr . DUP_TOP ROT_THREE COMPARE_OP JUMP_IF_FALSE_OR_POP compare_chained_right COME_FROM
compare_single ::= expr . expr COMPARE_OP
compare_single ::= expr expr . COMPARE_OP
compare_single ::= expr expr COMPARE_OP . 
continues ::= _stmts . lastc_stmt continue
continues ::= _stmts lastc_stmt . continue
continues ::= lastc_stmt . continue
dict ::= expr . expr expr LOAD_CONST BUILD_CONST_KEY_MAP_3
dict ::= expr expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_3
dict ::= expr expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_3
else_suite ::= suite_stmts . 
else_suitec ::= c_stmts . 
else_suitec ::= suite_stmts . 
except_ret38 ::= SETUP_FINALLY . expr ROT_FOUR POP_BLOCK POP_EXCEPT CALL_FINALLY RETURN_VALUE COME_FROM COME_FROM_FINALLY \e_suite_stmts_opt END_FINALLY
except_ret38 ::= SETUP_FINALLY . expr ROT_FOUR POP_BLOCK POP_EXCEPT CALL_FINALLY RETURN_VALUE COME_FROM COME_FROM_FINALLY suite_stmts_opt END_FINALLY
except_return_value ::= expr . POP_BLOCK RETURN_VALUE
expr ::= LOAD_CONST . 
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= LOAD_STR . 
expr ::= attribute . 
expr ::= attribute37 . 
expr ::= bin_op . 
expr ::= call . 
expr ::= compare . 
expr ::= if_exp . 
expr ::= list . 
expr ::= not . 
expr ::= subscript . 
expr_jifop ::= expr . JUMP_IF_FALSE_OR_POP
expr_jifop_cfs ::= expr . JUMP_IF_FALSE_OR_POP \e__come_froms
expr_jifop_cfs ::= expr . JUMP_IF_FALSE_OR_POP _come_froms
expr_jitop ::= expr . JUMP_IF_TRUE_OR_POP
expr_or_arg ::= expr . 
expr_pjif ::= expr . POP_JUMP_IF_FALSE
expr_pjif ::= expr POP_JUMP_IF_FALSE . 
expr_pjit ::= expr . POP_JUMP_IF_TRUE
expr_pjit ::= expr POP_JUMP_IF_TRUE . 
expr_pjitt ::= expr . pjump_ift
expr_stmt ::= expr . POP_TOP
expr_stmt ::= expr POP_TOP . 
for38 ::= expr . get_for_iter store for_block JUMP_LOOP \e__come_froms
for38 ::= expr . get_for_iter store for_block JUMP_LOOP \e__come_froms POP_BLOCK
for38 ::= expr . get_for_iter store for_block JUMP_LOOP _come_froms
for38 ::= expr . get_for_iter store for_block JUMP_LOOP _come_froms POP_BLOCK
for38 ::= expr . get_for_iter store for_block \e__come_froms
for38 ::= expr . get_for_iter store for_block _come_froms
for38 ::= expr . get_iter store for_block JUMP_LOOP \e__come_froms
for38 ::= expr . get_iter store for_block JUMP_LOOP _come_froms
for_iter ::= \e__come_froms . FOR_ITER
forelselaststmt38 ::= expr . get_for_iter store for_block else_suitec \e__come_froms
forelselaststmt38 ::= expr . get_for_iter store for_block else_suitec _come_froms
forelselaststmtc38 ::= expr . get_for_iter store for_block else_suitec \e__come_froms
forelselaststmtc38 ::= expr . get_for_iter store for_block else_suitec _come_froms
forelsestmt38 ::= expr . get_for_iter store for_block JUMP_LOOP \e__come_froms else_suite \e__come_froms
forelsestmt38 ::= expr . get_for_iter store for_block JUMP_LOOP \e__come_froms else_suite _come_froms
forelsestmt38 ::= expr . get_for_iter store for_block JUMP_LOOP _come_froms else_suite \e__come_froms
forelsestmt38 ::= expr . get_for_iter store for_block JUMP_LOOP _come_froms else_suite _come_froms
forelsestmt38 ::= expr . get_for_iter store for_block POP_BLOCK else_suite \e__come_froms
forelsestmt38 ::= expr . get_for_iter store for_block POP_BLOCK else_suite _come_froms
get_iter ::= expr . GET_ITER
if_and_elsestmtc ::= expr_pjif . expr_pjif c_stmts jb_cfs else_suitec \e_opt_come_from_except
if_and_elsestmtc ::= expr_pjif . expr_pjif c_stmts jb_cfs else_suitec opt_come_from_except
if_and_elsestmtc ::= expr_pjif expr_pjif . c_stmts jb_cfs else_suitec \e_opt_come_from_except
if_and_elsestmtc ::= expr_pjif expr_pjif . c_stmts jb_cfs else_suitec opt_come_from_except
if_and_elsestmtc ::= expr_pjif expr_pjif c_stmts . jb_cfs else_suitec \e_opt_come_from_except
if_and_elsestmtc ::= expr_pjif expr_pjif c_stmts . jb_cfs else_suitec opt_come_from_except
if_and_elsestmtc ::= expr_pjif expr_pjif c_stmts jb_cfs . else_suitec \e_opt_come_from_except
if_and_elsestmtc ::= expr_pjif expr_pjif c_stmts jb_cfs . else_suitec opt_come_from_except
if_and_elsestmtc ::= expr_pjif expr_pjif c_stmts jb_cfs else_suitec . opt_come_from_except
if_and_elsestmtc ::= expr_pjif expr_pjif c_stmts jb_cfs else_suitec \e_opt_come_from_except . 
if_and_elsestmtc ::= expr_pjif expr_pjif c_stmts jb_cfs else_suitec opt_come_from_except . 
if_and_stmt ::= expr_pjif . expr COME_FROM stmts \e__come_froms
if_and_stmt ::= expr_pjif . expr COME_FROM stmts _come_froms
if_and_stmt ::= expr_pjif expr . COME_FROM stmts \e__come_froms
if_and_stmt ::= expr_pjif expr . COME_FROM stmts _come_froms
if_exp ::= expr_pjif . expr jf_cf expr COME_FROM
if_exp ::= expr_pjif . expr jump_forward_else expr
if_exp ::= expr_pjif . expr jump_forward_else expr come_froms
if_exp ::= expr_pjif expr . jf_cf expr COME_FROM
if_exp ::= expr_pjif expr . jump_forward_else expr
if_exp ::= expr_pjif expr . jump_forward_else expr come_froms
if_exp ::= expr_pjif expr jf_cf . expr COME_FROM
if_exp ::= expr_pjif expr jf_cf expr . COME_FROM
if_exp ::= expr_pjif expr jf_cf expr COME_FROM . 
if_exp ::= expr_pjif expr jump_forward_else . expr
if_exp ::= expr_pjif expr jump_forward_else . expr come_froms
if_exp ::= expr_pjif expr jump_forward_else expr . 
if_exp ::= expr_pjif expr jump_forward_else expr . come_froms
if_exp ::= expr_pjif expr jump_forward_else expr come_froms . 
if_exp_37b ::= expr_pjif . expr_pjif jump_forward_else expr
if_exp_37b ::= expr_pjif expr_pjif . jump_forward_else expr
if_exp_compare ::= bool_op . expr jf_cfs expr COME_FROM
if_exp_compare ::= bool_op expr . jf_cfs expr COME_FROM
if_exp_compare ::= expr . expr jf_cfs expr COME_FROM
if_exp_compare ::= expr expr . jf_cfs expr COME_FROM
if_exp_compare38 ::= or_in_ifexp . jump_if_false_cf expr jf_cfs expr come_froms
if_exp_loop ::= expr_pjif . expr POP_JUMP_IF_FALSE_LOOP JUMP_FORWARD come_froms expr
if_exp_loop ::= expr_pjif expr . POP_JUMP_IF_FALSE_LOOP JUMP_FORWARD come_froms expr
if_exp_not ::= expr . POP_JUMP_IF_TRUE expr jump_forward_else expr COME_FROM
if_exp_not ::= expr POP_JUMP_IF_TRUE . expr jump_forward_else expr COME_FROM
if_exp_not ::= expr POP_JUMP_IF_TRUE expr . jump_forward_else expr COME_FROM
if_exp_true ::= expr . JUMP_FORWARD expr COME_FROM
if_exp_true ::= expr JUMP_FORWARD . expr COME_FROM
if_not_stmtc ::= testexprc . ifstmts_jumpc \e__come_froms
if_not_stmtc ::= testexprc . ifstmts_jumpc _come_froms
if_not_stmtc ::= testexprc ifstmts_jumpc . _come_froms
if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms . 
if_not_stmtc ::= testexprc ifstmts_jumpc _come_froms . 
if_or_not_elsestmt ::= expr . POP_JUMP_IF_TRUE \e_come_from_opt expr POP_JUMP_IF_TRUE come_froms stmts jf_cfs else_suite \e_opt_come_from_except
if_or_not_elsestmt ::= expr . POP_JUMP_IF_TRUE \e_come_from_opt expr POP_JUMP_IF_TRUE come_froms stmts jf_cfs else_suite opt_come_from_except
if_or_not_elsestmt ::= expr . POP_JUMP_IF_TRUE come_from_opt expr POP_JUMP_IF_TRUE come_froms stmts jf_cfs else_suite \e_opt_come_from_except
if_or_not_elsestmt ::= expr . POP_JUMP_IF_TRUE come_from_opt expr POP_JUMP_IF_TRUE come_froms stmts jf_cfs else_suite opt_come_from_except
if_or_not_elsestmt ::= expr POP_JUMP_IF_TRUE . come_from_opt expr POP_JUMP_IF_TRUE come_froms stmts jf_cfs else_suite \e_opt_come_from_except
if_or_not_elsestmt ::= expr POP_JUMP_IF_TRUE . come_from_opt expr POP_JUMP_IF_TRUE come_froms stmts jf_cfs else_suite opt_come_from_except
if_or_not_elsestmt ::= expr POP_JUMP_IF_TRUE \e_come_from_opt . expr POP_JUMP_IF_TRUE come_froms stmts jf_cfs else_suite \e_opt_come_from_except
if_or_not_elsestmt ::= expr POP_JUMP_IF_TRUE \e_come_from_opt . expr POP_JUMP_IF_TRUE come_froms stmts jf_cfs else_suite opt_come_from_except
if_or_not_elsestmt ::= expr POP_JUMP_IF_TRUE \e_come_from_opt expr . POP_JUMP_IF_TRUE come_froms stmts jf_cfs else_suite \e_opt_come_from_except
if_or_not_elsestmt ::= expr POP_JUMP_IF_TRUE \e_come_from_opt expr . POP_JUMP_IF_TRUE come_froms stmts jf_cfs else_suite opt_come_from_except
if_or_stmt ::= expr . POP_JUMP_IF_TRUE expr pop_jump come_froms stmts COME_FROM
if_or_stmt ::= expr POP_JUMP_IF_TRUE . expr pop_jump come_froms stmts COME_FROM
if_or_stmt ::= expr POP_JUMP_IF_TRUE expr . pop_jump come_froms stmts COME_FROM
ifelsestmt ::= bool_op . stmts_opt jf_cfs \e_else_suite_opt \e_opt_come_from_except
ifelsestmt ::= bool_op . stmts_opt jf_cfs \e_else_suite_opt opt_come_from_except
ifelsestmt ::= bool_op . stmts_opt jf_cfs else_suite_opt \e_opt_come_from_except
ifelsestmt ::= bool_op . stmts_opt jf_cfs else_suite_opt opt_come_from_except
ifelsestmt ::= bool_op \e_stmts_opt . jf_cfs \e_else_suite_opt \e_opt_come_from_except
ifelsestmt ::= bool_op \e_stmts_opt . jf_cfs \e_else_suite_opt opt_come_from_except
ifelsestmt ::= bool_op \e_stmts_opt . jf_cfs else_suite_opt \e_opt_come_from_except
ifelsestmt ::= bool_op \e_stmts_opt . jf_cfs else_suite_opt opt_come_from_except
ifelsestmt ::= bool_op stmts_opt . jf_cfs \e_else_suite_opt \e_opt_come_from_except
ifelsestmt ::= bool_op stmts_opt . jf_cfs \e_else_suite_opt opt_come_from_except
ifelsestmt ::= bool_op stmts_opt . jf_cfs else_suite_opt \e_opt_come_from_except
ifelsestmt ::= bool_op stmts_opt . jf_cfs else_suite_opt opt_come_from_except
ifelsestmt ::= testexpr . stmts_opt JUMP_FORWARD else_suite \e__come_froms
ifelsestmt ::= testexpr . stmts_opt JUMP_FORWARD else_suite _come_froms
ifelsestmt ::= testexpr . stmts_opt jf_cfs \e_else_suite_opt \e_opt_come_from_except
ifelsestmt ::= testexpr . stmts_opt jf_cfs \e_else_suite_opt opt_come_from_except
ifelsestmt ::= testexpr . stmts_opt jf_cfs else_suite_opt \e_opt_come_from_except
ifelsestmt ::= testexpr . stmts_opt jf_cfs else_suite_opt opt_come_from_except
ifelsestmt ::= testexpr \e_stmts_opt . JUMP_FORWARD else_suite \e__come_froms
ifelsestmt ::= testexpr \e_stmts_opt . JUMP_FORWARD else_suite _come_froms
ifelsestmt ::= testexpr \e_stmts_opt . jf_cfs \e_else_suite_opt \e_opt_come_from_except
ifelsestmt ::= testexpr \e_stmts_opt . jf_cfs \e_else_suite_opt opt_come_from_except
ifelsestmt ::= testexpr \e_stmts_opt . jf_cfs else_suite_opt \e_opt_come_from_except
ifelsestmt ::= testexpr \e_stmts_opt . jf_cfs else_suite_opt opt_come_from_except
ifelsestmt ::= testexpr stmts_opt . JUMP_FORWARD else_suite \e__come_froms
ifelsestmt ::= testexpr stmts_opt . JUMP_FORWARD else_suite _come_froms
ifelsestmt ::= testexpr stmts_opt . jf_cfs \e_else_suite_opt \e_opt_come_from_except
ifelsestmt ::= testexpr stmts_opt . jf_cfs \e_else_suite_opt opt_come_from_except
ifelsestmt ::= testexpr stmts_opt . jf_cfs else_suite_opt \e_opt_come_from_except
ifelsestmt ::= testexpr stmts_opt . jf_cfs else_suite_opt opt_come_from_except
ifelsestmtc ::= testexpr . c_stmts cf_pt else_suite
ifelsestmtc ::= testexpr . c_stmts come_froms else_suite
ifelsestmtc ::= testexpr . c_stmts_opt JUMP_FORWARD else_suite \e__come_froms
ifelsestmtc ::= testexpr . c_stmts_opt JUMP_FORWARD else_suite _come_froms
ifelsestmtc ::= testexpr . c_stmts_opt JUMP_FORWARD else_suitec
ifelsestmtc ::= testexpr . c_stmts_opt JUMP_LOOP else_suitec JUMP_LOOP
ifelsestmtc ::= testexpr . c_stmts_opt cf_jump_back else_suitec
ifelsestmtc ::= testexpr . c_stmts_opt jb_cfs else_suitec
ifelsestmtc ::= testexpr . c_stmts_opt jb_cfs else_suitec JUMP_LOOP come_froms
ifelsestmtc ::= testexpr . c_stmts_opt jump_forward_else else_suitec \e_opt_come_from_except
ifelsestmtc ::= testexpr . c_stmts_opt jump_forward_else else_suitec opt_come_from_except
ifelsestmtc ::= testexpr \e_c_stmts_opt . JUMP_FORWARD else_suite \e__come_froms
ifelsestmtc ::= testexpr \e_c_stmts_opt . JUMP_FORWARD else_suite _come_froms
ifelsestmtc ::= testexpr \e_c_stmts_opt . JUMP_FORWARD else_suitec
ifelsestmtc ::= testexpr \e_c_stmts_opt . JUMP_LOOP else_suitec JUMP_LOOP
ifelsestmtc ::= testexpr \e_c_stmts_opt . cf_jump_back else_suitec
ifelsestmtc ::= testexpr \e_c_stmts_opt . jb_cfs else_suitec
ifelsestmtc ::= testexpr \e_c_stmts_opt . jb_cfs else_suitec JUMP_LOOP come_froms
ifelsestmtc ::= testexpr \e_c_stmts_opt . jump_forward_else else_suitec \e_opt_come_from_except
ifelsestmtc ::= testexpr \e_c_stmts_opt . jump_forward_else else_suitec opt_come_from_except
ifelsestmtc ::= testexpr c_stmts . cf_pt else_suite
ifelsestmtc ::= testexpr c_stmts . come_froms else_suite
ifelsestmtc ::= testexpr c_stmts come_froms . else_suite
ifelsestmtc ::= testexpr c_stmts come_froms else_suite . 
ifelsestmtc ::= testexpr c_stmts_opt . JUMP_FORWARD else_suite \e__come_froms
ifelsestmtc ::= testexpr c_stmts_opt . JUMP_FORWARD else_suite _come_froms
ifelsestmtc ::= testexpr c_stmts_opt . JUMP_FORWARD else_suitec
ifelsestmtc ::= testexpr c_stmts_opt . JUMP_LOOP else_suitec JUMP_LOOP
ifelsestmtc ::= testexpr c_stmts_opt . cf_jump_back else_suitec
ifelsestmtc ::= testexpr c_stmts_opt . jb_cfs else_suitec
ifelsestmtc ::= testexpr c_stmts_opt . jb_cfs else_suitec JUMP_LOOP come_froms
ifelsestmtc ::= testexpr c_stmts_opt . jump_forward_else else_suitec \e_opt_come_from_except
ifelsestmtc ::= testexpr c_stmts_opt . jump_forward_else else_suitec opt_come_from_except
ifelsestmtc ::= testexpr c_stmts_opt JUMP_LOOP . else_suitec JUMP_LOOP
ifelsestmtc ::= testexpr c_stmts_opt jb_cfs . else_suitec
ifelsestmtc ::= testexpr c_stmts_opt jb_cfs . else_suitec JUMP_LOOP come_froms
ifelsestmtc ::= testexpr c_stmts_opt jb_cfs else_suitec . 
ifelsestmtc ::= testexpr c_stmts_opt jb_cfs else_suitec . JUMP_LOOP come_froms
ifelsestmtc ::= testexpr c_stmts_opt jb_cfs else_suitec JUMP_LOOP . come_froms
ifelsestmtc ::= testexpr c_stmts_opt jb_cfs else_suitec JUMP_LOOP come_froms . 
ifelsestmtr ::= testexpr . return_if_stmts returns
iflaststmt ::= testexpr . returns
iflaststmt ::= testexpr . stmts
iflaststmt ::= testexpr . stmts JUMP_FORWARD
iflaststmt ::= testexpr . stmts_opt JUMP_FORWARD
iflaststmt ::= testexpr \e_stmts_opt . JUMP_FORWARD
iflaststmt ::= testexpr returns . 
iflaststmt ::= testexpr stmts . 
iflaststmt ::= testexpr stmts . JUMP_FORWARD
iflaststmt ::= testexpr stmts_opt . JUMP_FORWARD
iflaststmtc ::= testexpr . c_stmts
iflaststmtc ::= testexpr . c_stmts JUMP_LOOP
iflaststmtc ::= testexpr . c_stmts JUMP_LOOP COME_FROM_LOOP
iflaststmtc ::= testexpr . c_stmts JUMP_LOOP POP_BLOCK
iflaststmtc ::= testexpr . c_stmts come_froms
iflaststmtc ::= testexpr c_stmts . 
iflaststmtc ::= testexpr c_stmts . JUMP_LOOP
iflaststmtc ::= testexpr c_stmts . JUMP_LOOP COME_FROM_LOOP
iflaststmtc ::= testexpr c_stmts . JUMP_LOOP POP_BLOCK
iflaststmtc ::= testexpr c_stmts . come_froms
iflaststmtc ::= testexpr c_stmts JUMP_LOOP . 
iflaststmtc ::= testexpr c_stmts JUMP_LOOP . COME_FROM_LOOP
iflaststmtc ::= testexpr c_stmts JUMP_LOOP . POP_BLOCK
iflaststmtc ::= testexpr c_stmts come_froms . 
iflaststmtc ::= testexprc . c_stmts
iflaststmtc ::= testexprc . c_stmts JUMP_LOOP COME_FROM_LOOP
iflaststmtc ::= testexprc . c_stmts JUMP_LOOP \e_opt_pop_block
iflaststmtc ::= testexprc . c_stmts JUMP_LOOP opt_pop_block
iflaststmtc ::= testexprc c_stmts . 
iflaststmtc ::= testexprc c_stmts . JUMP_LOOP COME_FROM_LOOP
iflaststmtc ::= testexprc c_stmts . JUMP_LOOP \e_opt_pop_block
iflaststmtc ::= testexprc c_stmts . JUMP_LOOP opt_pop_block
iflaststmtc ::= testexprc c_stmts JUMP_LOOP . COME_FROM_LOOP
iflaststmtc ::= testexprc c_stmts JUMP_LOOP . opt_pop_block
iflaststmtc ::= testexprc c_stmts JUMP_LOOP \e_opt_pop_block . 
ifpoplaststmtc ::= testexpr . POP_TOP \e_c_stmts_opt
ifpoplaststmtc ::= testexpr . POP_TOP c_stmts_opt
ifstmt ::= bool_op . stmts \e__come_froms
ifstmt ::= bool_op . stmts _come_froms
ifstmt ::= bool_op stmts . _come_froms
ifstmt ::= bool_op stmts \e__come_froms . 
ifstmt ::= bool_op stmts _come_froms . 
ifstmt ::= testexpr . ifstmts_jump \e__come_froms
ifstmt ::= testexpr . ifstmts_jump _come_froms
ifstmt ::= testexpr . stmts \e__come_froms
ifstmt ::= testexpr . stmts _come_froms
ifstmt ::= testexpr ifstmts_jump . _come_froms
ifstmt ::= testexpr ifstmts_jump \e__come_froms . 
ifstmt ::= testexpr ifstmts_jump _come_froms . 
ifstmt ::= testexpr stmts . _come_froms
ifstmt ::= testexpr stmts \e__come_froms . 
ifstmt ::= testexpr stmts _come_froms . 
ifstmtc ::= testexpr . ifstmts_jumpc
ifstmtc ::= testexpr ifstmts_jumpc . 
ifstmtc ::= testexprc . ifstmts_jumpc \e__come_froms
ifstmtc ::= testexprc . ifstmts_jumpc _come_froms
ifstmtc ::= testexprc ifstmts_jumpc . _come_froms
ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms . 
ifstmtc ::= testexprc ifstmts_jumpc _come_froms . 
ifstmts_jump ::= \e_stmts_opt . JUMP_FORWARD JUMP_FORWARD \e__come_froms
ifstmts_jump ::= \e_stmts_opt . JUMP_FORWARD JUMP_FORWARD _come_froms
ifstmts_jump ::= \e_stmts_opt . come_froms
ifstmts_jump ::= stmts . come_froms
ifstmts_jump ::= stmts come_froms . 
ifstmts_jump ::= stmts_opt . JUMP_FORWARD JUMP_FORWARD \e__come_froms
ifstmts_jump ::= stmts_opt . JUMP_FORWARD JUMP_FORWARD _come_froms
ifstmts_jump ::= stmts_opt . come_froms
ifstmts_jump ::= stmts_opt come_froms . 
ifstmts_jumpc ::= \e_c_stmts_opt . come_froms
ifstmts_jumpc ::= c_stmts . 
ifstmts_jumpc ::= c_stmts . JUMP_LOOP
ifstmts_jumpc ::= c_stmts JUMP_LOOP . 
ifstmts_jumpc ::= c_stmts_opt . come_froms
ifstmts_jumpc ::= c_stmts_opt come_froms . 
ifstmts_jumpc ::= ifstmts_jump . 
import ::= LOAD_CONST . LOAD_CONST alias
import_as37 ::= LOAD_CONST . LOAD_CONST importlist37 store POP_TOP
import_from ::= LOAD_CONST . LOAD_CONST IMPORT_NAME importlist POP_TOP
import_from ::= LOAD_CONST . LOAD_CONST importlist POP_TOP
import_from37 ::= LOAD_CONST . LOAD_CONST IMPORT_NAME_ATTR importlist37 POP_TOP
import_from_as37 ::= LOAD_CONST . LOAD_CONST import_from_attr37 store POP_TOP
import_from_star ::= LOAD_CONST . LOAD_CONST IMPORT_NAME IMPORT_STAR
import_from_star ::= LOAD_CONST . LOAD_CONST IMPORT_NAME_ATTR IMPORT_STAR
importmultiple ::= LOAD_CONST . LOAD_CONST alias imports_cont
inplace_op ::= INPLACE_ADD . 
jb_cfs ::= \e_come_from_opt . JUMP_LOOP come_froms
jb_cfs ::= \e_come_from_opt JUMP_LOOP . come_froms
jb_cfs ::= \e_come_from_opt JUMP_LOOP come_froms . 
jb_cfs ::= come_from_opt . JUMP_LOOP come_froms
jf_cf ::= JUMP_FORWARD . COME_FROM
jf_cf ::= JUMP_FORWARD COME_FROM . 
jump_forward_else ::= JUMP_FORWARD . _come_froms
jump_forward_else ::= JUMP_FORWARD \e__come_froms . 
jump_forward_else ::= JUMP_FORWARD _come_froms . 
jump_forward_else ::= come_froms . jump COME_FROM
lastc_stmt ::= ifelsestmtc . 
lc_body ::= expr . LIST_APPEND
lc_setup_finally ::= LOAD_CONST . SETUP_FINALLY
list ::= BUILD_LIST_0 . 
list ::= expr . expr expr BUILD_LIST_3
list ::= expr expr . expr BUILD_LIST_3
list ::= expr expr expr . BUILD_LIST_3
list_comp ::= BUILD_LIST_0 . list_iter
list_for ::= expr_or_arg . for_iter store list_iter jb_or_c \e__come_froms
list_for ::= expr_or_arg . for_iter store list_iter jb_or_c _come_froms
list_if ::= expr . jump_if_false_cf list_iter
list_if ::= expr . list_if_end list_iter \e_come_from_opt
list_if ::= expr . list_if_end list_iter come_from_opt
list_if ::= expr . pjump_iff list_iter \e_come_from_opt
list_if ::= expr . pjump_iff list_iter come_from_opt
list_if_not ::= expr . list_if_not_end list_iter \e_come_from_opt
list_if_not ::= expr . list_if_not_end list_iter come_from_opt
list_if_not38 ::= expr . pjump_ift expr pjump_ift \e__come_froms list_iter \e_come_from_opt
list_if_not38 ::= expr . pjump_ift expr pjump_ift \e__come_froms list_iter come_from_opt
list_if_not38 ::= expr . pjump_ift expr pjump_ift _come_froms list_iter \e_come_from_opt
list_if_not38 ::= expr . pjump_ift expr pjump_ift _come_froms list_iter come_from_opt
list_unpack ::= BUILD_LIST_0 . expr LIST_EXTEND
list_unpack ::= BUILD_LIST_0 expr . LIST_EXTEND
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
named_expr ::= expr . DUP_TOP store
nand ::= and_parts . expr_pjit come_froms
nor_cond ::= or_parts . expr_pjif
not ::= expr_pjit . 
not_and_not ::= not . expr_pjif COME_FROM
not_or ::= and_parts . expr_pjif \e__come_froms
not_or ::= and_parts . expr_pjif _come_froms
not_or ::= and_parts expr_pjif . _come_froms
not_or ::= and_parts expr_pjif \e__come_froms . 
opt_come_from_except ::= come_any_froms . 
or ::= expr_pjit . expr COME_FROM
or ::= expr_pjit . expr jump_if_false_cf
or ::= expr_pjit expr . COME_FROM
or ::= expr_pjit expr . jump_if_false_cf
or ::= or_parts . expr
or ::= or_parts expr . 
or_and1 ::= or_parts . and_parts come_froms
or_and_not ::= expr_pjit . and_not COME_FROM
or_cond ::= or_parts . expr_pjif come_froms
or_expr ::= expr . JUMP_IF_TRUE expr COME_FROM
or_in_ifexp ::= expr_pjit . expr
or_in_ifexp ::= expr_pjit expr . 
or_in_ifexp ::= or_in_ifexp . POP_JUMP_IF_TRUE expr
or_parts ::= expr_pjit . 
or_parts ::= or_parts . expr_pjit
pop_ex_return ::= return_expr . ROT_FOUR POP_EXCEPT RETURN_VALUE
popb_return ::= return_expr . POP_BLOCK RETURN_VALUE
return ::= return_expr . RETURN_END_IF
return ::= return_expr . RETURN_VALUE
return ::= return_expr . discard_tops RETURN_VALUE
return ::= return_expr RETURN_VALUE . 
return_except ::= stmts . POP_BLOCK return
return_expr ::= expr . 
return_if_stmt ::= return_expr . RETURN_END_IF
return_if_stmt ::= return_expr . RETURN_END_IF POP_BLOCK
return_if_stmts ::= _stmts . return_if_stmt \e__come_froms
return_if_stmts ::= _stmts . return_if_stmt _come_froms
returns ::= _stmts . return
returns ::= _stmts . return_if_stmt
returns ::= return . 
returns_in_except ::= _stmts . except_return_value
returns_in_except2 ::= _stmts . except_return_value2
sf_pb_call_returns ::= SETUP_FINALLY . POP_BLOCK CALL_FINALLY returns
sf_pb_call_returns ::= SETUP_FINALLY . POP_BLOCK POP_EXCEPT CALL_FINALLY returns
sstmt ::= return . RETURN_LAST
sstmt ::= sstmt . RETURN_LAST
sstmt ::= stmt . 
stmt ::= assign . 
stmt ::= aug_assign1 . 
stmt ::= break . 
stmt ::= expr_stmt . 
stmt ::= ifstmt . 
stmt ::= return . 
stmt ::= whileTruestmt38 . 
stmt ::= whilestmt38 . 
stmts ::= sstmt . 
stmts ::= stmt . 
stmts ::= stmts . last_stmt
stmts ::= stmts . sstmt
stmts ::= stmts . stmt
stmts ::= stmts sstmt . 
stmts ::= stmts stmt . 
stmts_opt ::= stmts . 
store ::= STORE_FAST . 
store ::= expr . STORE_ATTR
store ::= expr STORE_ATTR . 
store_subscript ::= expr . expr STORE_SUBSCR
store_subscript ::= expr expr . STORE_SUBSCR
subscript ::= expr . expr BINARY_SUBSCR
subscript ::= expr expr . BINARY_SUBSCR
subscript ::= expr expr BINARY_SUBSCR . 
subscript2 ::= expr . expr DUP_TOP_TWO BINARY_SUBSCR
subscript2 ::= expr expr . DUP_TOP_TWO BINARY_SUBSCR
suite_stmts ::= _stmts . 
suite_stmts_opt ::= suite_stmts . 
testexpr ::= testfalse . 
testexpr ::= testtrue . 
testexpr_cf ::= testexpr . come_froms
testexprc ::= testexpr . 
testfalse ::= expr_pjif . 
testfalsec ::= expr . POP_JUMP_IF_TRUE_LOOP
testtrue ::= expr_pjit . 
testtrue ::= or_in_ifexp . POP_JUMP_IF_TRUE
testtruec ::= expr . POP_JUMP_IF_FALSE_LOOP
try_elsestmtl38 ::= SETUP_FINALLY . suite_stmts_opt POP_BLOCK except_handler38 COME_FROM else_suitec \e_opt_come_from_except
try_elsestmtl38 ::= SETUP_FINALLY . suite_stmts_opt POP_BLOCK except_handler38 COME_FROM else_suitec opt_come_from_except
try_elsestmtl38 ::= SETUP_FINALLY \e_suite_stmts_opt . POP_BLOCK except_handler38 COME_FROM else_suitec \e_opt_come_from_except
try_elsestmtl38 ::= SETUP_FINALLY \e_suite_stmts_opt . POP_BLOCK except_handler38 COME_FROM else_suitec opt_come_from_except
try_elsestmtl38 ::= SETUP_FINALLY suite_stmts_opt . POP_BLOCK except_handler38 COME_FROM else_suitec \e_opt_come_from_except
try_elsestmtl38 ::= SETUP_FINALLY suite_stmts_opt . POP_BLOCK except_handler38 COME_FROM else_suitec opt_come_from_except
try_except ::= SETUP_FINALLY . suite_stmts_opt POP_BLOCK except_handler38
try_except ::= SETUP_FINALLY . suite_stmts_opt POP_BLOCK except_handler38 jump_excepts \e_come_from_except_clauses
try_except ::= SETUP_FINALLY . suite_stmts_opt POP_BLOCK except_handler38 jump_excepts come_from_except_clauses
try_except ::= SETUP_FINALLY \e_suite_stmts_opt . POP_BLOCK except_handler38
try_except ::= SETUP_FINALLY \e_suite_stmts_opt . POP_BLOCK except_handler38 jump_excepts \e_come_from_except_clauses
try_except ::= SETUP_FINALLY \e_suite_stmts_opt . POP_BLOCK except_handler38 jump_excepts come_from_except_clauses
try_except ::= SETUP_FINALLY suite_stmts_opt . POP_BLOCK except_handler38
try_except ::= SETUP_FINALLY suite_stmts_opt . POP_BLOCK except_handler38 jump_excepts \e_come_from_except_clauses
try_except ::= SETUP_FINALLY suite_stmts_opt . POP_BLOCK except_handler38 jump_excepts come_from_except_clauses
try_except38 ::= SETUP_FINALLY . POP_BLOCK POP_TOP \e_suite_stmts_opt except_handler38a
try_except38 ::= SETUP_FINALLY . POP_BLOCK POP_TOP suite_stmts_opt except_handler38a
try_except38 ::= SETUP_FINALLY . POP_BLOCK suite_stmts except_handler38b
try_except38r ::= SETUP_FINALLY . return_except except_handler38b
try_except38r2 ::= SETUP_FINALLY . suite_stmts_opt POP_BLOCK JUMP_FORWARD COME_FROM_FINALLY POP_TOP POP_TOP POP_TOP \e_cond_except_stmts_opt POP_EXCEPT return END_FINALLY COME_FROM
try_except38r2 ::= SETUP_FINALLY . suite_stmts_opt POP_BLOCK JUMP_FORWARD COME_FROM_FINALLY POP_TOP POP_TOP POP_TOP cond_except_stmts_opt POP_EXCEPT return END_FINALLY COME_FROM
try_except38r2 ::= SETUP_FINALLY \e_suite_stmts_opt . POP_BLOCK JUMP_FORWARD COME_FROM_FINALLY POP_TOP POP_TOP POP_TOP \e_cond_except_stmts_opt POP_EXCEPT return END_FINALLY COME_FROM
try_except38r2 ::= SETUP_FINALLY \e_suite_stmts_opt . POP_BLOCK JUMP_FORWARD COME_FROM_FINALLY POP_TOP POP_TOP POP_TOP cond_except_stmts_opt POP_EXCEPT return END_FINALLY COME_FROM
try_except38r2 ::= SETUP_FINALLY suite_stmts_opt . POP_BLOCK JUMP_FORWARD COME_FROM_FINALLY POP_TOP POP_TOP POP_TOP \e_cond_except_stmts_opt POP_EXCEPT return END_FINALLY COME_FROM
try_except38r2 ::= SETUP_FINALLY suite_stmts_opt . POP_BLOCK JUMP_FORWARD COME_FROM_FINALLY POP_TOP POP_TOP POP_TOP cond_except_stmts_opt POP_EXCEPT return END_FINALLY COME_FROM
try_except38r3 ::= SETUP_FINALLY . suite_stmts_opt POP_BLOCK JUMP_FORWARD COME_FROM_FINALLY \e_cond_except_stmts_opt POP_EXCEPT return COME_FROM END_FINALLY COME_FROM
try_except38r3 ::= SETUP_FINALLY . suite_stmts_opt POP_BLOCK JUMP_FORWARD COME_FROM_FINALLY cond_except_stmts_opt POP_EXCEPT return COME_FROM END_FINALLY COME_FROM
try_except38r3 ::= SETUP_FINALLY \e_suite_stmts_opt . POP_BLOCK JUMP_FORWARD COME_FROM_FINALLY \e_cond_except_stmts_opt POP_EXCEPT return COME_FROM END_FINALLY COME_FROM
try_except38r3 ::= SETUP_FINALLY \e_suite_stmts_opt . POP_BLOCK JUMP_FORWARD COME_FROM_FINALLY cond_except_stmts_opt POP_EXCEPT return COME_FROM END_FINALLY COME_FROM
try_except38r3 ::= SETUP_FINALLY suite_stmts_opt . POP_BLOCK JUMP_FORWARD COME_FROM_FINALLY \e_cond_except_stmts_opt POP_EXCEPT return COME_FROM END_FINALLY COME_FROM
try_except38r3 ::= SETUP_FINALLY suite_stmts_opt . POP_BLOCK JUMP_FORWARD COME_FROM_FINALLY cond_except_stmts_opt POP_EXCEPT return COME_FROM END_FINALLY COME_FROM
try_except38r4 ::= SETUP_FINALLY . returns_in_except COME_FROM_FINALLY except_cond1 return COME_FROM END_FINALLY
try_except38r5 ::= SETUP_FINALLY . returns_in_except COME_FROM_FINALLY except_cond1 except_ret38d COME_FROM END_FINALLY
try_except38r5 ::= SETUP_FINALLY . returns_in_except COME_FROM_FINALLY except_cond1 except_suite COME_FROM END_FINALLY COME_FROM
try_except38r5 ::= SETUP_FINALLY . returns_in_except COME_FROM_FINALLY except_cond2 except_ret38b END_FINALLY COME_FROM
try_except38r6 ::= SETUP_FINALLY . returns_in_except2 COME_FROM_FINALLY POP_TOP POP_TOP POP_TOP except_ret38d END_FINALLY
try_except38r7 ::= SETUP_FINALLY . suite_stmts_opt POP_BLOCK JUMP_FORWARD COME_FROM_FINALLY POP_TOP POP_TOP POP_TOP return_expr ROT_FOUR POP_EXCEPT POP_BLOCK ROT_TWO POP_TOP CALL_FINALLY RETURN_VALUE END_FINALLY COME_FROM POP_BLOCK BEGIN_FINALLY COME_FROM COME_FROM_FINALLY
try_except38r7 ::= SETUP_FINALLY \e_suite_stmts_opt . POP_BLOCK JUMP_FORWARD COME_FROM_FINALLY POP_TOP POP_TOP POP_TOP return_expr ROT_FOUR POP_EXCEPT POP_BLOCK ROT_TWO POP_TOP CALL_FINALLY RETURN_VALUE END_FINALLY COME_FROM POP_BLOCK BEGIN_FINALLY COME_FROM COME_FROM_FINALLY
try_except38r7 ::= SETUP_FINALLY suite_stmts_opt . POP_BLOCK JUMP_FORWARD COME_FROM_FINALLY POP_TOP POP_TOP POP_TOP return_expr ROT_FOUR POP_EXCEPT POP_BLOCK ROT_TWO POP_TOP CALL_FINALLY RETURN_VALUE END_FINALLY COME_FROM POP_BLOCK BEGIN_FINALLY COME_FROM COME_FROM_FINALLY
try_except_as ::= SETUP_FINALLY . POP_BLOCK suite_stmts except_handler_as END_FINALLY COME_FROM
try_except_as ::= SETUP_FINALLY . suite_stmts except_handler_as END_FINALLY COME_FROM
try_except_as ::= SETUP_FINALLY suite_stmts . except_handler_as END_FINALLY COME_FROM
try_except_ret38 ::= SETUP_FINALLY . returns except_ret38a
try_except_ret38a ::= SETUP_FINALLY . returns except_handler38c END_FINALLY \e_come_from_opt
try_except_ret38a ::= SETUP_FINALLY . returns except_handler38c END_FINALLY come_from_opt
tryfinally36 ::= SETUP_FINALLY . returns COME_FROM_FINALLY suite_stmts
tryfinally38_return ::= SETUP_FINALLY . suite_stmts_opt POP_BLOCK JUMP_FORWARD COME_FROM_FINALLY except_cond2 except_ret38c
tryfinally38_return ::= SETUP_FINALLY \e_suite_stmts_opt . POP_BLOCK JUMP_FORWARD COME_FROM_FINALLY except_cond2 except_ret38c
tryfinally38_return ::= SETUP_FINALLY suite_stmts_opt . POP_BLOCK JUMP_FORWARD COME_FROM_FINALLY except_cond2 except_ret38c
tryfinally38a_return ::= LOAD_CONST . SETUP_FINALLY \e_suite_stmts_opt except_return38 COME_FROM COME_FROM_FINALLY \e_suite_stmts_opt pop_finally_pt return END_FINALLY POP_TOP
tryfinally38a_return ::= LOAD_CONST . SETUP_FINALLY \e_suite_stmts_opt except_return38 COME_FROM COME_FROM_FINALLY suite_stmts_opt pop_finally_pt return END_FINALLY POP_TOP
tryfinally38a_return ::= LOAD_CONST . SETUP_FINALLY suite_stmts_opt except_return38 COME_FROM COME_FROM_FINALLY \e_suite_stmts_opt pop_finally_pt return END_FINALLY POP_TOP
tryfinally38a_return ::= LOAD_CONST . SETUP_FINALLY suite_stmts_opt except_return38 COME_FROM COME_FROM_FINALLY suite_stmts_opt pop_finally_pt return END_FINALLY POP_TOP
tryfinally38astmt ::= LOAD_CONST . SETUP_FINALLY \e_suite_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY POP_FINALLY POP_TOP \e_suite_stmts_opt END_FINALLY POP_TOP
tryfinally38astmt ::= LOAD_CONST . SETUP_FINALLY \e_suite_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY POP_FINALLY POP_TOP suite_stmts_opt END_FINALLY POP_TOP
tryfinally38astmt ::= LOAD_CONST . SETUP_FINALLY suite_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY POP_FINALLY POP_TOP \e_suite_stmts_opt END_FINALLY POP_TOP
tryfinally38astmt ::= LOAD_CONST . SETUP_FINALLY suite_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY POP_FINALLY POP_TOP suite_stmts_opt END_FINALLY POP_TOP
tryfinally38rstmt3 ::= SETUP_FINALLY . expr POP_BLOCK CALL_FINALLY RETURN_VALUE COME_FROM COME_FROM_FINALLY ss_end_finally
tryfinally38stmt ::= SETUP_FINALLY . suite_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM COME_FROM_FINALLY \e_suite_stmts_opt END_FINALLY
tryfinally38stmt ::= SETUP_FINALLY . suite_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM COME_FROM_FINALLY suite_stmts_opt END_FINALLY
tryfinally38stmt ::= SETUP_FINALLY . suite_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY POP_FINALLY \e_suite_stmts_opt END_FINALLY
tryfinally38stmt ::= SETUP_FINALLY . suite_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY POP_FINALLY suite_stmts_opt END_FINALLY
tryfinally38stmt ::= SETUP_FINALLY \e_suite_stmts_opt . POP_BLOCK BEGIN_FINALLY COME_FROM COME_FROM_FINALLY \e_suite_stmts_opt END_FINALLY
tryfinally38stmt ::= SETUP_FINALLY \e_suite_stmts_opt . POP_BLOCK BEGIN_FINALLY COME_FROM COME_FROM_FINALLY suite_stmts_opt END_FINALLY
tryfinally38stmt ::= SETUP_FINALLY \e_suite_stmts_opt . POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY POP_FINALLY \e_suite_stmts_opt END_FINALLY
tryfinally38stmt ::= SETUP_FINALLY \e_suite_stmts_opt . POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY POP_FINALLY suite_stmts_opt END_FINALLY
tryfinally38stmt ::= SETUP_FINALLY suite_stmts_opt . POP_BLOCK BEGIN_FINALLY COME_FROM COME_FROM_FINALLY \e_suite_stmts_opt END_FINALLY
tryfinally38stmt ::= SETUP_FINALLY suite_stmts_opt . POP_BLOCK BEGIN_FINALLY COME_FROM COME_FROM_FINALLY suite_stmts_opt END_FINALLY
tryfinally38stmt ::= SETUP_FINALLY suite_stmts_opt . POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY POP_FINALLY \e_suite_stmts_opt END_FINALLY
tryfinally38stmt ::= SETUP_FINALLY suite_stmts_opt . POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY POP_FINALLY suite_stmts_opt END_FINALLY
tryfinally_return_stmt1 ::= SETUP_FINALLY . suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_FINALLY returns
tryfinally_return_stmt1 ::= SETUP_FINALLY \e_suite_stmts_opt . POP_BLOCK LOAD_CONST COME_FROM_FINALLY returns
tryfinally_return_stmt1 ::= SETUP_FINALLY suite_stmts_opt . POP_BLOCK LOAD_CONST COME_FROM_FINALLY returns
tryfinally_return_stmt2 ::= SETUP_FINALLY . suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_FINALLY
tryfinally_return_stmt2 ::= SETUP_FINALLY \e_suite_stmts_opt . POP_BLOCK LOAD_CONST COME_FROM_FINALLY
tryfinally_return_stmt2 ::= SETUP_FINALLY suite_stmts_opt . POP_BLOCK LOAD_CONST COME_FROM_FINALLY
tryfinallystmt ::= SETUP_FINALLY . suite_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY \e_suite_stmts_opt END_FINALLY
tryfinallystmt ::= SETUP_FINALLY . suite_stmts_opt POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY suite_stmts_opt END_FINALLY
tryfinallystmt ::= SETUP_FINALLY \e_suite_stmts_opt . POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY \e_suite_stmts_opt END_FINALLY
tryfinallystmt ::= SETUP_FINALLY \e_suite_stmts_opt . POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY suite_stmts_opt END_FINALLY
tryfinallystmt ::= SETUP_FINALLY suite_stmts_opt . POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY \e_suite_stmts_opt END_FINALLY
tryfinallystmt ::= SETUP_FINALLY suite_stmts_opt . POP_BLOCK BEGIN_FINALLY COME_FROM_FINALLY suite_stmts_opt END_FINALLY
tryfinallystmt_break ::= SETUP_FINALLY . suite_stmts_opt POP_BLOCK POP_EXCEPT CALL_FINALLY JUMP_FORWARD POP_BLOCK BEGIN_FINALLY COME_FROM COME_FROM_FINALLY \e_suite_stmts_opt END_FINALLY
tryfinallystmt_break ::= SETUP_FINALLY . suite_stmts_opt POP_BLOCK POP_EXCEPT CALL_FINALLY JUMP_FORWARD POP_BLOCK BEGIN_FINALLY COME_FROM COME_FROM_FINALLY suite_stmts_opt END_FINALLY
tryfinallystmt_break ::= SETUP_FINALLY \e_suite_stmts_opt . POP_BLOCK POP_EXCEPT CALL_FINALLY JUMP_FORWARD POP_BLOCK BEGIN_FINALLY COME_FROM COME_FROM_FINALLY \e_suite_stmts_opt END_FINALLY
tryfinallystmt_break ::= SETUP_FINALLY \e_suite_stmts_opt . POP_BLOCK POP_EXCEPT CALL_FINALLY JUMP_FORWARD POP_BLOCK BEGIN_FINALLY COME_FROM COME_FROM_FINALLY suite_stmts_opt END_FINALLY
tryfinallystmt_break ::= SETUP_FINALLY suite_stmts_opt . POP_BLOCK POP_EXCEPT CALL_FINALLY JUMP_FORWARD POP_BLOCK BEGIN_FINALLY COME_FROM COME_FROM_FINALLY \e_suite_stmts_opt END_FINALLY
tryfinallystmt_break ::= SETUP_FINALLY suite_stmts_opt . POP_BLOCK POP_EXCEPT CALL_FINALLY JUMP_FORWARD POP_BLOCK BEGIN_FINALLY COME_FROM COME_FROM_FINALLY suite_stmts_opt END_FINALLY
unary_not ::= expr . UNARY_NOT
unary_op ::= expr . unary_operator
while1stmt ::= \e__come_froms . c_stmts COME_FROM JUMP_LOOP COME_FROM_LOOP
while1stmt ::= \e__come_froms . c_stmts COME_FROM_LOOP
while1stmt ::= \e__come_froms c_stmts . COME_FROM JUMP_LOOP COME_FROM_LOOP
while1stmt ::= \e__come_froms c_stmts . COME_FROM_LOOP
while1stmt ::= \e__come_froms c_stmts COME_FROM . JUMP_LOOP COME_FROM_LOOP
while1stmt ::= _come_froms . c_stmts COME_FROM JUMP_LOOP COME_FROM_LOOP
while1stmt ::= _come_froms . c_stmts COME_FROM_LOOP
while1stmt ::= _come_froms c_stmts . COME_FROM JUMP_LOOP COME_FROM_LOOP
while1stmt ::= _come_froms c_stmts . COME_FROM_LOOP
while1stmt ::= _come_froms c_stmts COME_FROM . JUMP_LOOP COME_FROM_LOOP
whileTruestmt ::= \e__come_froms . c_stmts JUMP_LOOP \e__come_froms POP_BLOCK
whileTruestmt ::= \e__come_froms . c_stmts JUMP_LOOP _come_froms POP_BLOCK
whileTruestmt ::= \e__come_froms c_stmts . JUMP_LOOP \e__come_froms POP_BLOCK
whileTruestmt ::= \e__come_froms c_stmts . JUMP_LOOP _come_froms POP_BLOCK
whileTruestmt ::= \e__come_froms c_stmts JUMP_LOOP . _come_froms POP_BLOCK
whileTruestmt ::= \e__come_froms c_stmts JUMP_LOOP \e__come_froms . POP_BLOCK
whileTruestmt ::= \e__come_froms c_stmts JUMP_LOOP _come_froms . POP_BLOCK
whileTruestmt ::= _come_froms . c_stmts JUMP_LOOP \e__come_froms POP_BLOCK
whileTruestmt ::= _come_froms . c_stmts JUMP_LOOP _come_froms POP_BLOCK
whileTruestmt ::= _come_froms c_stmts . JUMP_LOOP \e__come_froms POP_BLOCK
whileTruestmt ::= _come_froms c_stmts . JUMP_LOOP _come_froms POP_BLOCK
whileTruestmt ::= _come_froms c_stmts JUMP_LOOP . _come_froms POP_BLOCK
whileTruestmt ::= _come_froms c_stmts JUMP_LOOP \e__come_froms . POP_BLOCK
whileTruestmt ::= _come_froms c_stmts JUMP_LOOP _come_froms . POP_BLOCK
whileTruestmt38 ::= \e__come_froms . c_stmts JUMP_LOOP COME_FROM_EXCEPT_CLAUSE
whileTruestmt38 ::= \e__come_froms . c_stmts JUMP_LOOP \e__come_froms
whileTruestmt38 ::= \e__come_froms . c_stmts JUMP_LOOP _come_froms
whileTruestmt38 ::= \e__come_froms . pass JUMP_LOOP
whileTruestmt38 ::= \e__come_froms \e_pass . JUMP_LOOP
whileTruestmt38 ::= \e__come_froms \e_pass JUMP_LOOP . 
whileTruestmt38 ::= \e__come_froms c_stmts . JUMP_LOOP COME_FROM_EXCEPT_CLAUSE
whileTruestmt38 ::= \e__come_froms c_stmts . JUMP_LOOP \e__come_froms
whileTruestmt38 ::= \e__come_froms c_stmts . JUMP_LOOP _come_froms
whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP . COME_FROM_EXCEPT_CLAUSE
whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP . _come_froms
whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP \e__come_froms . 
whileTruestmt38 ::= \e__come_froms c_stmts JUMP_LOOP _come_froms . 
whileTruestmt38 ::= _come_froms . c_stmts JUMP_LOOP COME_FROM_EXCEPT_CLAUSE
whileTruestmt38 ::= _come_froms . c_stmts JUMP_LOOP \e__come_froms
whileTruestmt38 ::= _come_froms . c_stmts JUMP_LOOP _come_froms
whileTruestmt38 ::= _come_froms . pass JUMP_LOOP
whileTruestmt38 ::= _come_froms \e_pass . JUMP_LOOP
whileTruestmt38 ::= _come_froms c_stmts . JUMP_LOOP COME_FROM_EXCEPT_CLAUSE
whileTruestmt38 ::= _come_froms c_stmts . JUMP_LOOP \e__come_froms
whileTruestmt38 ::= _come_froms c_stmts . JUMP_LOOP _come_froms
whileTruestmt38 ::= _come_froms c_stmts JUMP_LOOP . COME_FROM_EXCEPT_CLAUSE
whileTruestmt38 ::= _come_froms c_stmts JUMP_LOOP . _come_froms
whileTruestmt38 ::= _come_froms c_stmts JUMP_LOOP \e__come_froms . 
whileTruestmt38 ::= _come_froms c_stmts JUMP_LOOP _come_froms . 
whilestmt38 ::= \e__come_froms . bool_op c_stmts JUMP_LOOP \e__come_froms
whilestmt38 ::= \e__come_froms . bool_op c_stmts JUMP_LOOP _come_froms
whilestmt38 ::= \e__come_froms . testexpr \e_c_stmts_opt COME_FROM JUMP_LOOP POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr \e_c_stmts_opt JUMP_LOOP POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr \e_c_stmts_opt JUMP_LOOP come_froms
whilestmt38 ::= \e__come_froms . testexpr c_stmts JUMP_LOOP \e__come_froms
whilestmt38 ::= \e__come_froms . testexpr c_stmts JUMP_LOOP _come_froms
whilestmt38 ::= \e__come_froms . testexpr c_stmts come_froms
whilestmt38 ::= \e__come_froms . testexpr c_stmts_opt COME_FROM JUMP_LOOP POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr c_stmts_opt JUMP_LOOP POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr c_stmts_opt JUMP_LOOP come_froms
whilestmt38 ::= \e__come_froms . testexpr returns POP_BLOCK
whilestmt38 ::= \e__come_froms . testexprc \e_c_stmts_opt come_froms JUMP_LOOP \e__come_froms
whilestmt38 ::= \e__come_froms . testexprc \e_c_stmts_opt come_froms JUMP_LOOP _come_froms
whilestmt38 ::= \e__come_froms . testexprc c_stmts_opt come_froms JUMP_LOOP \e__come_froms
whilestmt38 ::= \e__come_froms . testexprc c_stmts_opt come_froms JUMP_LOOP _come_froms
whilestmt38 ::= \e__come_froms bool_op . c_stmts JUMP_LOOP \e__come_froms
whilestmt38 ::= \e__come_froms bool_op . c_stmts JUMP_LOOP _come_froms
whilestmt38 ::= \e__come_froms bool_op c_stmts . JUMP_LOOP \e__come_froms
whilestmt38 ::= \e__come_froms bool_op c_stmts . JUMP_LOOP _come_froms
whilestmt38 ::= \e__come_froms testexpr . c_stmts JUMP_LOOP \e__come_froms
whilestmt38 ::= \e__come_froms testexpr . c_stmts JUMP_LOOP _come_froms
whilestmt38 ::= \e__come_froms testexpr . c_stmts come_froms
whilestmt38 ::= \e__come_froms testexpr . c_stmts_opt COME_FROM JUMP_LOOP POP_BLOCK
whilestmt38 ::= \e__come_froms testexpr . c_stmts_opt JUMP_LOOP POP_BLOCK
whilestmt38 ::= \e__come_froms testexpr . c_stmts_opt JUMP_LOOP come_froms
whilestmt38 ::= \e__come_froms testexpr . returns POP_BLOCK
whilestmt38 ::= \e__come_froms testexpr \e_c_stmts_opt . COME_FROM JUMP_LOOP POP_BLOCK
whilestmt38 ::= \e__come_froms testexpr \e_c_stmts_opt . JUMP_LOOP POP_BLOCK
whilestmt38 ::= \e__come_froms testexpr \e_c_stmts_opt . JUMP_LOOP come_froms
whilestmt38 ::= \e__come_froms testexpr c_stmts . JUMP_LOOP \e__come_froms
whilestmt38 ::= \e__come_froms testexpr c_stmts . JUMP_LOOP _come_froms
whilestmt38 ::= \e__come_froms testexpr c_stmts . come_froms
whilestmt38 ::= \e__come_froms testexpr c_stmts JUMP_LOOP . _come_froms
whilestmt38 ::= \e__come_froms testexpr c_stmts JUMP_LOOP \e__come_froms . 
whilestmt38 ::= \e__come_froms testexpr c_stmts JUMP_LOOP _come_froms . 
whilestmt38 ::= \e__come_froms testexpr c_stmts come_froms . 
whilestmt38 ::= \e__come_froms testexpr c_stmts_opt . COME_FROM JUMP_LOOP POP_BLOCK
whilestmt38 ::= \e__come_froms testexpr c_stmts_opt . JUMP_LOOP POP_BLOCK
whilestmt38 ::= \e__come_froms testexpr c_stmts_opt . JUMP_LOOP come_froms
whilestmt38 ::= \e__come_froms testexpr c_stmts_opt COME_FROM . JUMP_LOOP POP_BLOCK
whilestmt38 ::= \e__come_froms testexpr c_stmts_opt JUMP_LOOP . POP_BLOCK
whilestmt38 ::= \e__come_froms testexpr c_stmts_opt JUMP_LOOP . come_froms
whilestmt38 ::= \e__come_froms testexpr c_stmts_opt JUMP_LOOP come_froms . 
whilestmt38 ::= \e__come_froms testexpr returns . POP_BLOCK
whilestmt38 ::= \e__come_froms testexprc . c_stmts_opt come_froms JUMP_LOOP \e__come_froms
whilestmt38 ::= \e__come_froms testexprc . c_stmts_opt come_froms JUMP_LOOP _come_froms
whilestmt38 ::= \e__come_froms testexprc \e_c_stmts_opt . come_froms JUMP_LOOP \e__come_froms
whilestmt38 ::= \e__come_froms testexprc \e_c_stmts_opt . come_froms JUMP_LOOP _come_froms
whilestmt38 ::= \e__come_froms testexprc c_stmts_opt . come_froms JUMP_LOOP \e__come_froms
whilestmt38 ::= \e__come_froms testexprc c_stmts_opt . come_froms JUMP_LOOP _come_froms
whilestmt38 ::= \e__come_froms testexprc c_stmts_opt come_froms . JUMP_LOOP \e__come_froms
whilestmt38 ::= \e__come_froms testexprc c_stmts_opt come_froms . JUMP_LOOP _come_froms
whilestmt38 ::= _come_froms . bool_op c_stmts JUMP_LOOP \e__come_froms
whilestmt38 ::= _come_froms . bool_op c_stmts JUMP_LOOP _come_froms
whilestmt38 ::= _come_froms . testexpr \e_c_stmts_opt COME_FROM JUMP_LOOP POP_BLOCK
whilestmt38 ::= _come_froms . testexpr \e_c_stmts_opt JUMP_LOOP POP_BLOCK
whilestmt38 ::= _come_froms . testexpr \e_c_stmts_opt JUMP_LOOP come_froms
whilestmt38 ::= _come_froms . testexpr c_stmts JUMP_LOOP \e__come_froms
whilestmt38 ::= _come_froms . testexpr c_stmts JUMP_LOOP _come_froms
whilestmt38 ::= _come_froms . testexpr c_stmts come_froms
whilestmt38 ::= _come_froms . testexpr c_stmts_opt COME_FROM JUMP_LOOP POP_BLOCK
whilestmt38 ::= _come_froms . testexpr c_stmts_opt JUMP_LOOP POP_BLOCK
whilestmt38 ::= _come_froms . testexpr c_stmts_opt JUMP_LOOP come_froms
whilestmt38 ::= _come_froms . testexpr returns POP_BLOCK
whilestmt38 ::= _come_froms . testexprc \e_c_stmts_opt come_froms JUMP_LOOP \e__come_froms
whilestmt38 ::= _come_froms . testexprc \e_c_stmts_opt come_froms JUMP_LOOP _come_froms
whilestmt38 ::= _come_froms . testexprc c_stmts_opt come_froms JUMP_LOOP \e__come_froms
whilestmt38 ::= _come_froms . testexprc c_stmts_opt come_froms JUMP_LOOP _come_froms
whilestmt38 ::= _come_froms testexpr . c_stmts JUMP_LOOP \e__come_froms
whilestmt38 ::= _come_froms testexpr . c_stmts JUMP_LOOP _come_froms
whilestmt38 ::= _come_froms testexpr . c_stmts come_froms
whilestmt38 ::= _come_froms testexpr . c_stmts_opt COME_FROM JUMP_LOOP POP_BLOCK
whilestmt38 ::= _come_froms testexpr . c_stmts_opt JUMP_LOOP POP_BLOCK
whilestmt38 ::= _come_froms testexpr . c_stmts_opt JUMP_LOOP come_froms
whilestmt38 ::= _come_froms testexpr . returns POP_BLOCK
whilestmt38 ::= _come_froms testexpr \e_c_stmts_opt . COME_FROM JUMP_LOOP POP_BLOCK
whilestmt38 ::= _come_froms testexpr \e_c_stmts_opt . JUMP_LOOP POP_BLOCK
whilestmt38 ::= _come_froms testexpr \e_c_stmts_opt . JUMP_LOOP come_froms
whilestmt38 ::= _come_froms testexpr c_stmts . JUMP_LOOP \e__come_froms
whilestmt38 ::= _come_froms testexpr c_stmts . JUMP_LOOP _come_froms
whilestmt38 ::= _come_froms testexpr c_stmts . come_froms
whilestmt38 ::= _come_froms testexpr c_stmts JUMP_LOOP . _come_froms
whilestmt38 ::= _come_froms testexpr c_stmts JUMP_LOOP \e__come_froms . 
whilestmt38 ::= _come_froms testexpr c_stmts JUMP_LOOP _come_froms . 
whilestmt38 ::= _come_froms testexpr c_stmts come_froms . 
whilestmt38 ::= _come_froms testexpr c_stmts_opt . COME_FROM JUMP_LOOP POP_BLOCK
whilestmt38 ::= _come_froms testexpr c_stmts_opt . JUMP_LOOP POP_BLOCK
whilestmt38 ::= _come_froms testexpr c_stmts_opt . JUMP_LOOP come_froms
whilestmt38 ::= _come_froms testexpr c_stmts_opt COME_FROM . JUMP_LOOP POP_BLOCK
whilestmt38 ::= _come_froms testexpr c_stmts_opt JUMP_LOOP . POP_BLOCK
whilestmt38 ::= _come_froms testexpr c_stmts_opt JUMP_LOOP . come_froms
whilestmt38 ::= _come_froms testexpr c_stmts_opt JUMP_LOOP come_froms . 
whilestmt38 ::= _come_froms testexprc . c_stmts_opt come_froms JUMP_LOOP \e__come_froms
whilestmt38 ::= _come_froms testexprc . c_stmts_opt come_froms JUMP_LOOP _come_froms
whilestmt38 ::= _come_froms testexprc \e_c_stmts_opt . come_froms JUMP_LOOP \e__come_froms
whilestmt38 ::= _come_froms testexprc \e_c_stmts_opt . come_froms JUMP_LOOP _come_froms
whilestmt38 ::= _come_froms testexprc c_stmts_opt . come_froms JUMP_LOOP \e__come_froms
whilestmt38 ::= _come_froms testexprc c_stmts_opt . come_froms JUMP_LOOP _come_froms
whilestmt38 ::= _come_froms testexprc c_stmts_opt come_froms . JUMP_LOOP \e__come_froms
whilestmt38 ::= _come_froms testexprc c_stmts_opt come_froms . JUMP_LOOP _come_froms
yield ::= expr . YIELD_VALUE
yield_from ::= expr . GET_YIELD_FROM_ITER LOAD_CONST YIELD_FROM
Instruction context:
-> 
 L.  57         0  LOAD_FAST                'self'
                   2  LOAD_ATTR                init_sent
                   4  POP_JUMP_IF_TRUE     10  'to 10'
               expr ::= LOAD_FAST (1)
               return_expr ::= expr (1)
               attribute ::= expr LOAD_ATTR (2)
               expr ::= attribute (2)
               return_expr ::= expr (2)
               expr_pjit ::= expr POP_JUMP_IF_TRUE (3)
               testtrue ::= expr_pjit (3)
               not ::= expr_pjit (3)
               or_parts ::= expr_pjit (3)
               testexpr ::= testtrue (3)
               expr ::= not (3)
               testexprc ::= testexpr (3)
               return_expr ::= expr (3)
L.119:   6     expr ::= LOAD_CONST (4)
L.119:   6     expr ::= LOAD_CONST (4)
               or_in_ifexp ::= expr_pjit expr (4)
               or ::= or_parts expr (4)
Reduce or invalid by check
L.119:   6     return_expr ::= expr (4)
L.119:   6-8   return ::= return_expr RETURN_VALUE (5)
L.119:   6     returns ::= return (5)
L.119:   6     stmt ::= return (5)
               iflaststmt ::= testexpr returns (5)
Reduce iflaststmt invalid by check
L.119:   6     c_returns ::= returns (5)
L.119:   6     stmts ::= stmt (5)
L.119:   6     c_stmt ::= stmt (5)
L.119:   6     sstmt ::= stmt (5)
L.119:   6     c_stmts ::= c_returns (5)
               ifstmt ::= testexpr stmts \e__come_froms (5)
               iflaststmt ::= testexpr stmts (5)
Reduce iflaststmt invalid by check
L.119:   6     stmts_opt ::= stmts (5)
L.119:   6     _stmts ::= stmts (5)
L.119:   6     c_stmts ::= c_stmt (5)
L.119:   6     stmts ::= sstmt (5)
               iflaststmtc ::= testexpr c_stmts (5)
Reduce iflaststmtc invalid by check
L.119:   6     c_stmts_opt ::= c_stmts (5)
L.119:   6     ifstmts_jumpc ::= c_stmts (5)
               iflaststmtc ::= testexprc c_stmts (5)
Reduce iflaststmtc invalid by check
               stmt ::= ifstmt (5)
L.119:   6     c_stmts ::= _stmts (5)
               ifstmtc ::= testexpr ifstmts_jumpc (5)
               ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms (5)
               if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms (5)
Reduce if_not_stmtc invalid by check
               stmts ::= stmt (5)
               c_stmt ::= stmt (5)
               sstmt ::= stmt (5)
               c_stmt ::= ifstmtc (5)
               START ::= |- stmts (5)
               _stmts ::= stmts (5)
               c_stmts ::= c_stmt (5)
               stmts ::= sstmt (5)
               c_stmts ::= _stmts (5)
        10-10  _come_froms ::= \e__come_froms COME_FROM (6)
        10     come_froms ::= COME_FROM (6)
        10-10  _come_froms ::= \e__come_froms COME_FROM (6)
        10     come_froms ::= COME_FROM (6)
        10     come_froms ::= COME_FROM (6)
        10     come_from_opt ::= COME_FROM (6)
        10     come_froms ::= COME_FROM (6)
               ifstmt ::= testexpr stmts _come_froms (6)
               ifstmtc ::= testexprc ifstmts_jumpc _come_froms (6)
               if_not_stmtc ::= testexprc ifstmts_jumpc _come_froms (6)
Reduce if_not_stmtc invalid by check
L.119:   6-10  ifstmts_jump ::= stmts come_froms (6)
               whilestmt38 ::= \e__come_froms testexpr c_stmts come_froms (6)
Reduce whilestmt38 invalid by check
               iflaststmtc ::= testexpr c_stmts come_froms (6)
Reduce iflaststmtc invalid by check
L.119:   6-10  ifstmts_jump ::= stmts_opt come_froms (6)
L.119:   6-10  ifstmts_jumpc ::= c_stmts_opt come_froms (6)
               stmt ::= ifstmt (6)
               c_stmt ::= ifstmtc (6)
               ifstmt ::= testexpr ifstmts_jump \e__come_froms (6)
L.119:   6     ifstmts_jumpc ::= ifstmts_jump (6)
               ifstmtc ::= testexpr ifstmts_jumpc (6)
               ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms (6)
               if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms (6)
Reduce if_not_stmtc invalid by check
               stmts ::= stmt (6)
               c_stmt ::= stmt (6)
               sstmt ::= stmt (6)
               c_stmts ::= c_stmt (6)
               START ::= |- stmts (6)
               _stmts ::= stmts (6)
               stmts ::= sstmt (6)
               c_stmts ::= _stmts (6)
L.122:  10     expr ::= LOAD_FAST (7)
L.122:  10     return_expr ::= expr (7)
L.122:  10     return_expr ::= expr (7)
L.122:  10-12  attribute ::= expr LOAD_ATTR (8)
L.122:  10     expr ::= attribute (8)
L.122:  10     return_expr ::= expr (8)
L.122:  10     return_expr ::= expr (8)
L.122:  10-14  attribute37 ::= expr LOAD_METHOD (9)
L.122:  10     expr ::= attribute37 (9)
L.122:  10     return_expr ::= expr (9)
L.122:  10     return_expr ::= expr (9)
        16     expr ::= LOAD_GLOBAL (10)
        18     expr ::= LOAD_STR (11)
        16-20  subscript ::= expr expr BINARY_SUBSCR (12)
        16     expr ::= subscript (12)
L.122:  10-22  call ::= expr expr CALL_METHOD_1 (13)
L.122:  10     expr ::= call (13)
L.122:  10     return_expr ::= expr (13)
L.122:  10     return_expr ::= expr (13)
L.122:  10-24  expr_stmt ::= expr POP_TOP (14)
L.122:  10     stmt ::= expr_stmt (14)
L.122:  10     stmts ::= stmt (14)
L.122:  10     c_stmt ::= stmt (14)
L.122:  10     sstmt ::= stmt (14)
               stmts ::= stmts stmt (14)
L.122:  10     _stmts ::= stmts (14)
L.122:  10     c_stmts ::= c_stmt (14)
               c_stmts ::= c_stmts c_stmt (14)
L.122:  10     stmts ::= sstmt (14)
               stmts ::= stmts sstmt (14)
               START ::= |- stmts (14)
               _stmts ::= stmts (14)
L.122:  10     c_stmts ::= _stmts (14)
L.122:  10     suite_stmts ::= _stmts (14)
L.122:  10     c_stmts ::= _stmts (14)
               c_stmts ::= _stmts (14)
L.122:  10     else_suite ::= suite_stmts (14)
               ifelsestmtc ::= testexpr c_stmts come_froms else_suite (14)
               lastc_stmt ::= ifelsestmtc (14)
Reduce lastc_stmt invalid by check
               c_stmt ::= ifelsestmtc (14)
               c_stmts ::= c_stmt (14)
L.124:  26     expr ::= LOAD_FAST (15)
L.124:  26     return_expr ::= expr (15)
L.124:  26     return_expr ::= expr (15)
L.124:  26-28  attribute ::= expr LOAD_ATTR (16)
L.124:  26     expr ::= attribute (16)
L.124:  26     return_expr ::= expr (16)
L.124:  26     return_expr ::= expr (16)
L.124:  26-30  attribute37 ::= expr LOAD_METHOD (17)
L.124:  26     expr ::= attribute37 (17)
L.124:  26     return_expr ::= expr (17)
L.124:  26     return_expr ::= expr (17)
        32     expr ::= LOAD_FAST (18)
        32-34  attribute ::= expr LOAD_ATTR (19)
        32     expr ::= attribute (19)
        32-36  attribute37 ::= expr LOAD_METHOD (20)
        32     expr ::= attribute37 (20)
        32-38  call ::= expr CALL_METHOD_0 (21)
        32     expr ::= call (21)
        40     expr ::= LOAD_CONST (22)
        42     binary_operator ::= BINARY_ADD (23)
        32-42  bin_op ::= expr expr binary_operator (23)
        32     expr ::= bin_op (23)
L.124:  26-44  call ::= expr expr CALL_METHOD_1 (24)
L.124:  26     expr ::= call (24)
L.124:  26     return_expr ::= expr (24)
L.124:  26     return_expr ::= expr (24)
               expr_stmt ::= expr POP_TOP (25)
               stmt ::= expr_stmt (25)
               stmts ::= stmts stmt (25)
               stmts ::= stmt (25)
               c_stmt ::= stmt (25)
               sstmt ::= stmt (25)
               stmts ::= stmts stmt (25)
               _stmts ::= stmts (25)
               _stmts ::= stmts (25)
               c_stmts ::= c_stmt (25)
               c_stmts ::= c_stmts c_stmt (25)
               c_stmts ::= c_stmts c_stmt (25)
               stmts ::= stmts sstmt (25)
               stmts ::= sstmt (25)
               stmts ::= stmts sstmt (25)
               START ::= |- stmts (25)
               _stmts ::= stmts (25)
               c_stmts ::= _stmts (25)
               suite_stmts ::= _stmts (25)
               c_stmts ::= _stmts (25)
               c_stmts ::= _stmts (25)
               c_stmts ::= _stmts (25)
               else_suite ::= suite_stmts (25)
               ifelsestmtc ::= testexpr c_stmts come_froms else_suite (25)
               lastc_stmt ::= ifelsestmtc (25)
Reduce lastc_stmt invalid by check
               c_stmt ::= ifelsestmtc (25)
               c_stmts ::= c_stmt (25)
               expr ::= LOAD_FAST (1)
               return_expr ::= expr (1)
               attribute ::= expr LOAD_ATTR (2)
               expr ::= attribute (2)
               return_expr ::= expr (2)
               attribute37 ::= expr LOAD_METHOD (3)
               expr ::= attribute37 (3)
               return_expr ::= expr (3)
         6     expr ::= LOAD_GLOBAL (4)
         8     expr ::= LOAD_STR (5)
         6-10  subscript ::= expr expr BINARY_SUBSCR (6)
         6     expr ::= subscript (6)
               call ::= expr expr CALL_METHOD_1 (7)
               expr ::= call (7)
               return_expr ::= expr (7)
               expr_stmt ::= expr POP_TOP (8)
               stmt ::= expr_stmt (8)
               stmts ::= stmt (8)
               sstmt ::= stmt (8)
               c_stmt ::= stmt (8)
               START ::= |- stmts (8)
               _stmts ::= stmts (8)
               stmts ::= sstmt (8)
               c_stmts ::= c_stmt (8)
               c_stmts ::= _stmts (8)
L.130:  16     expr ::= LOAD_FAST (9)
L.130:  16     return_expr ::= expr (9)
L.130:  16     return_expr ::= expr (9)
L.130:  16-18  attribute ::= expr LOAD_ATTR (10)
L.130:  16     expr ::= attribute (10)
L.130:  16     return_expr ::= expr (10)
L.130:  16     return_expr ::= expr (10)
L.130:  16-20  attribute37 ::= expr LOAD_METHOD (11)
L.130:  16     expr ::= attribute37 (11)
L.130:  16     return_expr ::= expr (11)
L.130:  16     return_expr ::= expr (11)
        22     expr ::= LOAD_FAST (12)
        22-24  attribute ::= expr LOAD_ATTR (13)
        22     expr ::= attribute (13)
        22-26  attribute37 ::= expr LOAD_METHOD (14)
        22     expr ::= attribute37 (14)
        22-28  call ::= expr CALL_METHOD_0 (15)
        22     expr ::= call (15)
        30     expr ::= LOAD_CONST (16)
        32     binary_operator ::= BINARY_ADD (17)
        22-32  bin_op ::= expr expr binary_operator (17)
        22     expr ::= bin_op (17)
L.130:  16-34  call ::= expr expr CALL_METHOD_1 (18)
L.130:  16     expr ::= call (18)
L.130:  16     return_expr ::= expr (18)
L.130:  16     return_expr ::= expr (18)
L.130:  16-36  expr_stmt ::= expr POP_TOP (19)
L.130:  16     stmt ::= expr_stmt (19)
               stmts ::= stmts stmt (19)
L.130:  16     stmts ::= stmt (19)
L.130:  16     sstmt ::= stmt (19)
L.130:  16     c_stmt ::= stmt (19)
               START ::= |- stmts (19)
               _stmts ::= stmts (19)
L.130:  16     _stmts ::= stmts (19)
               stmts ::= stmts sstmt (19)
L.130:  16     stmts ::= sstmt (19)
L.130:  16     c_stmts ::= c_stmt (19)
               c_stmts ::= c_stmts c_stmt (19)
               c_stmts ::= _stmts (19)
L.130:  16     c_stmts ::= _stmts (19)
L.131:  38     expr ::= LOAD_CONST (20)
L.131:  38     expr ::= LOAD_CONST (20)
L.131:  38     return_expr ::= expr (20)
L.131:  38     return_expr ::= expr (20)
        40     expr ::= LOAD_FAST (21)
        40-42  store ::= expr STORE_ATTR (22)
L.131:  38-42  assign ::= expr store (22)
L.131:  38     stmt ::= assign (22)
               stmts ::= stmts stmt (22)
L.131:  38     stmts ::= stmt (22)
L.131:  38     sstmt ::= stmt (22)
L.131:  38     c_stmt ::= stmt (22)
L.130:  16-42  stmts ::= stmts stmt (22)
               START ::= |- stmts (22)
               _stmts ::= stmts (22)
L.131:  38     _stmts ::= stmts (22)
               stmts ::= stmts sstmt (22)
L.131:  38     stmts ::= sstmt (22)
L.130:  16-42  stmts ::= stmts sstmt (22)
L.131:  38     c_stmts ::= c_stmt (22)
L.130:  16-42  c_stmts ::= c_stmts c_stmt (22)
               c_stmts ::= c_stmts c_stmt (22)
L.130:  16     _stmts ::= stmts (22)
               c_stmts ::= _stmts (22)
L.131:  38     c_stmts ::= _stmts (22)
L.130:  16     c_stmts ::= _stmts (22)
L.133:  44     expr ::= LOAD_FAST (23)
L.133:  44     return_expr ::= expr (23)
L.133:  44     return_expr ::= expr (23)
L.133:  44-46  attribute37 ::= expr LOAD_METHOD (24)
L.133:  44     expr ::= attribute37 (24)
L.133:  44     return_expr ::= expr (24)
L.133:  44     return_expr ::= expr (24)
L.133:  44-48  call ::= expr CALL_METHOD_0 (25)
L.133:  44     expr ::= call (25)
L.133:  44     return_expr ::= expr (25)
L.133:  44     return_expr ::= expr (25)
L.133:  44-50  expr_pjif ::= expr POP_JUMP_IF_FALSE (26)
L.133:  44-50  expr_pjif ::= expr POP_JUMP_IF_FALSE (26)
L.133:  44     testfalse ::= expr_pjif (26)
L.133:  44     and_parts ::= expr_pjif (26)
L.133:  44     testfalse ::= expr_pjif (26)
L.133:  44     and_parts ::= expr_pjif (26)
L.133:  44     testexpr ::= testfalse (26)
L.133:  44     testexprc ::= testexpr (26)
L.133:  44     testexprc ::= testexpr (26)
L.134:  52     expr ::= LOAD_GLOBAL (27)
L.134:  52     return_expr ::= expr (27)
L.134:  52-54  attribute37 ::= expr LOAD_METHOD (28)
L.134:  52     expr ::= attribute37 (28)
L.134:  52     return_expr ::= expr (28)
        56     expr ::= LOAD_STR (29)
L.135:  58     expr ::= LOAD_STR (30)
        60     expr ::= LOAD_FAST (31)
        60-62  attribute ::= expr LOAD_ATTR (32)
        60     expr ::= attribute (32)
        64     expr ::= LOAD_FAST (33)
        64-66  attribute ::= expr LOAD_ATTR (34)
        64     expr ::= attribute (34)
        60-68  tuple ::= expr expr BUILD_TUPLE_2 (35)
        60     expr ::= tuple (35)
        70     binary_operator ::= BINARY_MODULO (36)
L.135:  58-70  bin_op ::= expr expr binary_operator (36)
L.135:  58     expr ::= bin_op (36)
L.134:  72     binary_operator ::= BINARY_ADD (37)
        56-72  bin_op ::= expr expr binary_operator (37)
        56     expr ::= bin_op (37)
L.134:  52-74  call ::= expr expr CALL_METHOD_1 (38)
L.134:  52     expr ::= call (38)
L.134:  52     return_expr ::= expr (38)
L.134:  52-76  expr_stmt ::= expr POP_TOP (39)
L.134:  52     stmt ::= expr_stmt (39)
L.134:  52     stmts ::= stmt (39)
L.134:  52     sstmt ::= stmt (39)
L.134:  52     c_stmt ::= stmt (39)
L.133:  44-76  ifstmt ::= testexpr stmts \e__come_froms (39)
L.133:  44-76  iflaststmt ::= testexpr stmts (39)
Reduce iflaststmt invalid by check
L.134:  52     stmts_opt ::= stmts (39)
L.134:  52     _stmts ::= stmts (39)
L.134:  52     _stmts ::= stmts (39)
L.134:  52     stmts ::= sstmt (39)
L.134:  52     c_stmts ::= c_stmt (39)
L.133:  44     stmt ::= ifstmt (39)
L.134:  52     c_stmts ::= _stmts (39)
L.134:  52     c_stmts ::= _stmts (39)
L.133:  44-76  iflaststmtc ::= testexpr c_stmts (39)
Reduce iflaststmtc invalid by check
L.134:  52     c_stmts_opt ::= c_stmts (39)
L.134:  52     ifstmts_jumpc ::= c_stmts (39)
L.133:  44-76  iflaststmtc ::= testexpr c_stmts (39)
Reduce iflaststmtc invalid by check
L.134:  52     c_stmts_opt ::= c_stmts (39)
L.133:  44-76  iflaststmtc ::= testexprc c_stmts (39)
Reduce iflaststmtc invalid by check
               stmts ::= stmts stmt (39)
L.133:  44     stmts ::= stmt (39)
L.133:  44     sstmt ::= stmt (39)
L.133:  44     c_stmt ::= stmt (39)
L.131:  38-76  stmts ::= stmts stmt (39)
L.130:  16-76  stmts ::= stmts stmt (39)
L.133:  44-76  ifstmtc ::= testexpr ifstmts_jumpc (39)
L.133:  44-76  ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms (39)
L.133:  44-76  if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms (39)
Reduce if_not_stmtc invalid by check
               START ::= |- stmts (39)
               _stmts ::= stmts (39)
L.133:  44     _stmts ::= stmts (39)
               stmts ::= stmts sstmt (39)
L.133:  44     stmts ::= sstmt (39)
L.131:  38-76  stmts ::= stmts sstmt (39)
L.130:  16-76  stmts ::= stmts sstmt (39)
L.133:  44     c_stmts ::= c_stmt (39)
L.131:  38-76  c_stmts ::= c_stmts c_stmt (39)
L.130:  16-76  c_stmts ::= c_stmts c_stmt (39)
               c_stmts ::= c_stmts c_stmt (39)
L.131:  38     _stmts ::= stmts (39)
L.130:  16     _stmts ::= stmts (39)
L.133:  44     c_stmt ::= ifstmtc (39)
               c_stmts ::= _stmts (39)
L.133:  44     c_stmts ::= _stmts (39)
L.131:  38     c_stmts ::= _stmts (39)
L.130:  16     c_stmts ::= _stmts (39)
               _come_froms ::= \e__come_froms COME_FROM (40)
               come_froms ::= COME_FROM (40)
               _come_froms ::= \e__come_froms COME_FROM (40)
               come_froms ::= COME_FROM (40)
               come_froms ::= COME_FROM (40)
               come_from_opt ::= COME_FROM (40)
               come_froms ::= COME_FROM (40)
               ifstmt ::= testexpr stmts _come_froms (40)
L.133:  44-78  ifstmtc ::= testexprc ifstmts_jumpc _come_froms (40)
L.133:  44-78  if_not_stmtc ::= testexprc ifstmts_jumpc _come_froms (40)
Reduce if_not_stmtc invalid by check
L.134:  52-78  ifstmts_jump ::= stmts come_froms (40)
L.134:  52-78  ifstmts_jump ::= stmts_opt come_froms (40)
L.133:  44-78  whilestmt38 ::= \e__come_froms testexpr c_stmts come_froms (40)
Reduce whilestmt38 invalid by check
L.133:  44-78  iflaststmtc ::= testexpr c_stmts come_froms (40)
Reduce iflaststmtc invalid by check
L.133:  44-78  iflaststmtc ::= testexpr c_stmts come_froms (40)
Reduce iflaststmtc invalid by check
L.134:  52-78  ifstmts_jumpc ::= c_stmts_opt come_froms (40)
L.133:  44     stmt ::= ifstmt (40)
L.133:  44     c_stmt ::= ifstmtc (40)
L.133:  44-78  ifstmt ::= testexpr ifstmts_jump \e__come_froms (40)
L.134:  52     ifstmts_jumpc ::= ifstmts_jump (40)
L.133:  44-78  ifstmtc ::= testexpr ifstmts_jumpc (40)
L.133:  44-78  ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms (40)
L.133:  44-78  if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms (40)
Reduce if_not_stmtc invalid by check
               stmts ::= stmts stmt (40)
L.133:  44     stmts ::= stmt (40)
L.133:  44     sstmt ::= stmt (40)
L.133:  44     c_stmt ::= stmt (40)
L.131:  38-78  stmts ::= stmts stmt (40)
L.130:  16-78  stmts ::= stmts stmt (40)
L.133:  44     c_stmts ::= c_stmt (40)
L.131:  38-78  c_stmts ::= c_stmts c_stmt (40)
L.130:  16-78  c_stmts ::= c_stmts c_stmt (40)
               c_stmts ::= c_stmts c_stmt (40)
               START ::= |- stmts (40)
               _stmts ::= stmts (40)
L.133:  44     _stmts ::= stmts (40)
               stmts ::= stmts sstmt (40)
L.133:  44     stmts ::= sstmt (40)
L.131:  38-78  stmts ::= stmts sstmt (40)
L.130:  16-78  stmts ::= stmts sstmt (40)
L.131:  38     _stmts ::= stmts (40)
L.130:  16     _stmts ::= stmts (40)
               c_stmts ::= _stmts (40)
L.133:  44     c_stmts ::= _stmts (40)
L.131:  38     c_stmts ::= _stmts (40)
L.130:  16     c_stmts ::= _stmts (40)
               expr ::= LOAD_FAST (1)
               return_expr ::= expr (1)
               attribute37 ::= expr LOAD_METHOD (2)
               expr ::= attribute37 (2)
               return_expr ::= expr (2)
               call ::= expr CALL_METHOD_0 (3)
               expr ::= call (3)
               return_expr ::= expr (3)
               expr_pjit ::= expr POP_JUMP_IF_TRUE (4)
               testtrue ::= expr_pjit (4)
               not ::= expr_pjit (4)
               or_parts ::= expr_pjit (4)
               testexpr ::= testtrue (4)
               expr ::= not (4)
               testexprc ::= testexpr (4)
               return_expr ::= expr (4)
L.139:   8     expr ::= LOAD_CONST (5)
L.139:   8     expr ::= LOAD_CONST (5)
               or_in_ifexp ::= expr_pjit expr (5)
               or ::= or_parts expr (5)
Reduce or invalid by check
L.139:   8     return_expr ::= expr (5)
        12     expr ::= LOAD_FAST (7)
        12-14  store ::= expr STORE_ATTR (8)
L.139:   8-14  named_expr ::= expr DUP_TOP store (8)
L.139:   8     expr ::= named_expr (8)
               or_in_ifexp ::= expr_pjit expr (8)
               or ::= or_parts expr (8)
Reduce or invalid by check
L.139:   8     return_expr ::= expr (8)
        16     expr ::= LOAD_FAST (9)
        16-18  store ::= expr STORE_ATTR (10)
        12-18  designList ::= store store (10)
L.139:   8-18  assign ::= expr store (10)
L.139:   8-18  assign ::= expr DUP_TOP designList (10)
L.139:   8     stmt ::= assign (10)
L.139:   8     stmts ::= stmt (10)
L.139:   8     c_stmt ::= stmt (10)
L.139:   8     sstmt ::= stmt (10)
               ifstmt ::= testexpr stmts \e__come_froms (10)
Reduce ifstmt invalid by check
               iflaststmt ::= testexpr stmts (10)
Reduce iflaststmt invalid by check
L.139:   8     stmts_opt ::= stmts (10)
L.139:   8     _stmts ::= stmts (10)
L.139:   8     c_stmts ::= c_stmt (10)
L.139:   8     stmts ::= sstmt (10)
L.139:   8     c_stmts ::= _stmts (10)
               iflaststmtc ::= testexpr c_stmts (10)
Reduce iflaststmtc invalid by check
L.139:   8     c_stmts_opt ::= c_stmts (10)
L.139:   8     ifstmts_jumpc ::= c_stmts (10)
               iflaststmtc ::= testexprc c_stmts (10)
Reduce iflaststmtc invalid by check
               ifstmtc ::= testexpr ifstmts_jumpc (10)
Reduce ifstmtc invalid by check
               ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms (10)
Reduce ifstmtc invalid by check
               if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms (10)
               c_stmt ::= if_not_stmtc (10)
               c_stmts ::= c_stmt (10)
L.140:  20     expr ::= LOAD_FAST (11)
L.140:  20     return_expr ::= expr (11)
L.140:  20     return_expr ::= expr (11)
L.140:  20-22  attribute ::= expr LOAD_ATTR (12)
L.140:  20     expr ::= attribute (12)
L.140:  20     return_expr ::= expr (12)
L.140:  20     return_expr ::= expr (12)
L.140:  20-24  attribute ::= expr LOAD_ATTR (13)
L.140:  20     expr ::= attribute (13)
L.140:  20     return_expr ::= expr (13)
L.140:  20     return_expr ::= expr (13)
L.140:  20-26  return ::= return_expr RETURN_VALUE (14)
L.140:  20     stmt ::= return (14)
L.140:  20     returns ::= return (14)
L.139:   8-26  returns ::= _stmts return (14)
L.139:   8-26  c_returns ::= c_stmts return (14)
               c_returns ::= c_stmts return (14)
L.139:   8-26  stmts ::= stmts stmt (14)
L.140:  20     stmts ::= stmt (14)
L.140:  20     c_stmt ::= stmt (14)
L.140:  20     sstmt ::= stmt (14)
L.140:  20     c_returns ::= returns (14)
               iflaststmt ::= testexpr returns (14)
Reduce iflaststmt invalid by check
L.139:   8     c_returns ::= returns (14)
L.139:   8     c_stmts ::= c_returns (14)
               c_stmts ::= c_returns (14)
               ifstmt ::= testexpr stmts \e__come_froms (14)
               iflaststmt ::= testexpr stmts (14)
Reduce iflaststmt invalid by check
L.139:   8     stmts_opt ::= stmts (14)
L.139:   8     _stmts ::= stmts (14)
L.140:  20     _stmts ::= stmts (14)
L.140:  20     c_stmts ::= c_stmt (14)
L.139:   8-26  c_stmts ::= c_stmts c_stmt (14)
               c_stmts ::= c_stmts c_stmt (14)
L.139:   8-26  stmts ::= stmts sstmt (14)
L.140:  20     stmts ::= sstmt (14)
L.140:  20     c_stmts ::= c_returns (14)
               iflaststmtc ::= testexpr c_stmts (14)
Reduce iflaststmtc invalid by check
L.139:   8     c_stmts_opt ::= c_stmts (14)
L.139:   8     ifstmts_jumpc ::= c_stmts (14)
               iflaststmtc ::= testexprc c_stmts (14)
Reduce iflaststmtc invalid by check
               stmt ::= ifstmt (14)
L.139:   8     c_stmts ::= _stmts (14)
L.140:  20     c_stmts ::= _stmts (14)
               ifstmtc ::= testexpr ifstmts_jumpc (14)
               ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms (14)
               if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms (14)
Reduce if_not_stmtc invalid by check
               stmts ::= stmt (14)
               c_stmt ::= stmt (14)
               sstmt ::= stmt (14)
               c_stmt ::= ifstmtc (14)
               START ::= |- stmts (14)
               _stmts ::= stmts (14)
               c_stmts ::= c_stmt (14)
               stmts ::= sstmt (14)
               c_stmts ::= _stmts (14)
        28-28  _come_froms ::= \e__come_froms COME_FROM (15)
        28     come_froms ::= COME_FROM (15)
        28-28  _come_froms ::= \e__come_froms COME_FROM (15)
        28     come_froms ::= COME_FROM (15)
        28     come_froms ::= COME_FROM (15)
        28     come_from_opt ::= COME_FROM (15)
        28     come_froms ::= COME_FROM (15)
               ifstmt ::= testexpr stmts _come_froms (15)
               ifstmtc ::= testexprc ifstmts_jumpc _come_froms (15)
               if_not_stmtc ::= testexprc ifstmts_jumpc _come_froms (15)
Reduce if_not_stmtc invalid by check
L.139:   8-28  ifstmts_jump ::= stmts come_froms (15)
               whilestmt38 ::= \e__come_froms testexpr c_stmts come_froms (15)
Reduce whilestmt38 invalid by check
               iflaststmtc ::= testexpr c_stmts come_froms (15)
Reduce iflaststmtc invalid by check
L.139:   8-28  ifstmts_jump ::= stmts_opt come_froms (15)
L.139:   8-28  ifstmts_jumpc ::= c_stmts_opt come_froms (15)
               stmt ::= ifstmt (15)
               c_stmt ::= ifstmtc (15)
               ifstmt ::= testexpr ifstmts_jump \e__come_froms (15)
L.139:   8     ifstmts_jumpc ::= ifstmts_jump (15)
               ifstmtc ::= testexpr ifstmts_jumpc (15)
               ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms (15)
               if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms (15)
Reduce if_not_stmtc invalid by check
               stmts ::= stmt (15)
               c_stmt ::= stmt (15)
               sstmt ::= stmt (15)
               c_stmts ::= c_stmt (15)
               START ::= |- stmts (15)
               _stmts ::= stmts (15)
               stmts ::= sstmt (15)
               c_stmts ::= _stmts (15)
L.142:  28     expr ::= LOAD_FAST (16)
L.142:  28     return_expr ::= expr (16)
L.142:  28     return_expr ::= expr (16)
L.142:  28-30  attribute ::= expr LOAD_ATTR (17)
L.142:  28     expr ::= attribute (17)
L.142:  28     return_expr ::= expr (17)
L.142:  28     return_expr ::= expr (17)
        32     expr ::= LOAD_FAST (18)
        32-34  attribute ::= expr LOAD_ATTR (19)
        32     expr ::= attribute (19)
L.142:  28-36  compare_single ::= expr expr COMPARE_OP (20)
L.142:  28     compare ::= compare_single (20)
L.142:  28     expr ::= compare (20)
L.142:  28     return_expr ::= expr (20)
L.142:  28     return_expr ::= expr (20)
L.142:  28-38  expr_pjit ::= expr POP_JUMP_IF_TRUE (21)
L.142:  28-38  expr_pjit ::= expr POP_JUMP_IF_TRUE (21)
L.142:  28     testtrue ::= expr_pjit (21)
L.142:  28     not ::= expr_pjit (21)
L.142:  28     or_parts ::= expr_pjit (21)
L.142:  28     testexpr ::= testtrue (21)
L.142:  28     testexpr ::= testtrue (21)
L.142:  28     expr ::= not (21)
L.142:  28     testexprc ::= testexpr (21)
L.142:  28     testexprc ::= testexpr (21)
L.142:  28     return_expr ::= expr (21)
L.142:  28     return_expr ::= expr (21)
        40     expr ::= LOAD_FAST (22)
L.142:  28-40  or_in_ifexp ::= expr_pjit expr (22)
L.142:  28-40  or ::= or_parts expr (22)
Reduce or invalid by check
        40     return_expr ::= expr (22)
        40-42  attribute ::= expr LOAD_ATTR (23)
        40     expr ::= attribute (23)
L.142:  28-42  or_in_ifexp ::= expr_pjit expr (23)
L.142:  28-42  or ::= or_parts expr (23)
Reduce or invalid by check
        40     return_expr ::= expr (23)
        44     expr ::= LOAD_FAST (24)
        44-46  attribute ::= expr LOAD_ATTR (25)
        44     expr ::= attribute (25)
        40-48  compare_single ::= expr expr COMPARE_OP (26)
        40     compare ::= compare_single (26)
        40     expr ::= compare (26)
L.142:  28-48  or_in_ifexp ::= expr_pjit expr (26)
L.142:  28-48  or ::= or_parts expr (26)
Reduce or invalid by check
        40     return_expr ::= expr (26)
        50     pop_jump ::= POP_JUMP_IF_FALSE (27)
        40-50  expr_pjif ::= expr POP_JUMP_IF_FALSE (27)
        40-50  expr_pjif ::= expr POP_JUMP_IF_FALSE (27)
        40     and_parts ::= expr_pjif (27)
        40     testfalse ::= expr_pjif (27)
L.142:  28-50  nor_cond ::= or_parts expr_pjif (27)
        40     testfalse ::= expr_pjif (27)
        40     and_parts ::= expr_pjif (27)
        40     testexpr ::= testfalse (27)
L.142:  28     testtrue ::= nor_cond (27)
        40     testexprc ::= testexpr (27)
L.142:  28     testexpr ::= testtrue (27)
L.142:  28     testexpr ::= testtrue (27)
L.142:  28     testexprc ::= testexpr (27)
L.142:  28     testexprc ::= testexpr (27)
        50-52  jump_if_false_cf ::= POP_JUMP_IF_FALSE COME_FROM (28)
        52     come_froms ::= COME_FROM (28)
L.142:  28-52  not_and_not ::= not expr_pjif COME_FROM (28)
        52     come_froms ::= COME_FROM (28)
        52     come_from_opt ::= COME_FROM (28)
        52-52  _come_froms ::= \e__come_froms COME_FROM (28)
        52     come_froms ::= COME_FROM (28)
        52-52  _come_froms ::= \e__come_froms COME_FROM (28)
        52-52  _come_froms ::= \e__come_froms COME_FROM (28)
        52     come_froms ::= COME_FROM (28)
        52     come_from_opt ::= COME_FROM (28)
        52-52  _come_froms ::= \e__come_froms COME_FROM (28)
        52     come_froms ::= COME_FROM (28)
        52-52  _come_froms ::= \e__come_froms COME_FROM (28)
L.142:  28-52  or ::= expr_pjit expr jump_if_false_cf (28)
Reduce or invalid by check
L.142:  28-52  or_cond ::= or_parts expr_pjif come_froms (28)
L.142:  28-52  or_and1 ::= or_parts and_parts come_froms (28)
        40-52  testexpr_cf ::= testexpr come_froms (28)
        52-52  ifstmts_jump ::= \e_stmts_opt come_froms (28)
Reduce ifstmts_jump invalid by check
        52-52  ifstmts_jumpc ::= \e_c_stmts_opt come_froms (28)
        52-52  ifstmts_jumpc ::= \e_c_stmts_opt come_froms (28)
        52-52  ifstmts_jump ::= \e_stmts_opt come_froms (28)
Reduce ifstmts_jump invalid by check
L.142:  28-52  testexpr_cf ::= testexpr come_froms (28)
L.142:  28     testfalse ::= or_cond (28)
        40-52  ifstmtc ::= testexpr ifstmts_jumpc (28)
Reduce ifstmtc invalid by check
        40-52  ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms (28)
Reduce ifstmtc invalid by check
        40-52  if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms (28)
L.142:  28-52  ifstmtc ::= testexpr ifstmts_jumpc (28)
Reduce ifstmtc invalid by check
L.142:  28-52  ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms (28)
Reduce ifstmtc invalid by check
L.142:  28-52  if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms (28)
L.142:  28     testexpr ::= testfalse (28)
        40     c_stmt ::= if_not_stmtc (28)
L.142:  28     c_stmt ::= if_not_stmtc (28)
L.142:  28     testexprc ::= testexpr (28)
L.142:  28     testexprc ::= testexpr (28)
        40     c_stmts ::= c_stmt (28)
L.142:  28     c_stmts ::= c_stmt (28)
               c_stmts ::= c_stmts c_stmt (28)
        40     c_stmts_opt ::= c_stmts (28)
L.142:  28-52  iflaststmtc ::= testexpr c_stmts (28)
Reduce iflaststmtc invalid by check
        40     c_stmts_opt ::= c_stmts (28)
        40     ifstmts_jumpc ::= c_stmts (28)
L.142:  28-52  iflaststmtc ::= testexpr c_stmts (28)
Reduce iflaststmtc invalid by check
L.142:  28-52  iflaststmtc ::= testexprc c_stmts (28)
Reduce iflaststmtc invalid by check
L.143:  52     expr ::= LOAD_FAST (29)
L.143:  52     return_expr ::= expr (29)
L.143:  52-54  attribute ::= expr LOAD_ATTR (30)
L.143:  52     expr ::= attribute (30)
L.143:  52     return_expr ::= expr (30)
L.143:  52-56  attribute37 ::= expr LOAD_METHOD (31)
L.143:  52     expr ::= attribute37 (31)
L.143:  52     return_expr ::= expr (31)
L.144:  58     expr ::= LOAD_STR (32)
L.145:  60     expr ::= LOAD_FAST (33)
L.145:  60-62  attribute ::= expr LOAD_ATTR (34)
L.145:  60     expr ::= attribute (34)
        64     expr ::= LOAD_FAST (35)
        64-66  attribute ::= expr LOAD_ATTR (36)
        64     expr ::= attribute (36)
        68     expr ::= LOAD_FAST (37)
        68-70  attribute ::= expr LOAD_ATTR (38)
        68     expr ::= attribute (38)
L.145:  60-72  tuple ::= expr expr expr BUILD_TUPLE_3 (39)
L.145:  60     expr ::= tuple (39)
L.144:  74     binary_operator ::= BINARY_MODULO (40)
L.144:  58-74  bin_op ::= expr expr binary_operator (40)
L.144:  58     expr ::= bin_op (40)
L.143:  52-76  call ::= expr expr CALL_METHOD_1 (41)
L.143:  52     expr ::= call (41)
L.143:  52     return_expr ::= expr (41)
L.143:  52-78  expr_stmt ::= expr POP_TOP (42)
L.143:  52     stmt ::= expr_stmt (42)
L.143:  52     stmts ::= stmt (42)
L.143:  52     c_stmt ::= stmt (42)
L.143:  52     sstmt ::= stmt (42)
L.143:  52     _stmts ::= stmts (42)
L.142:  28-78  ifstmt ::= testexpr stmts \e__come_froms (42)
L.142:  28-78  iflaststmt ::= testexpr stmts (42)
Reduce iflaststmt invalid by check
L.143:  52     stmts_opt ::= stmts (42)
L.143:  52     _stmts ::= stmts (42)
L.143:  52     c_stmts ::= c_stmt (42)
        40-78  c_stmts ::= c_stmts c_stmt (42)
L.142:  28-78  c_stmts ::= c_stmts c_stmt (42)
               c_stmts ::= c_stmts c_stmt (42)
L.143:  52     stmts ::= sstmt (42)
L.143:  52     c_stmts ::= _stmts (42)
L.143:  52     c_stmts ::= _stmts (42)
L.142:  28     stmt ::= ifstmt (42)
L.143:  52     c_stmts_opt ::= c_stmts (42)
L.142:  28-78  iflaststmtc ::= testexpr c_stmts (42)
Reduce iflaststmtc invalid by check
L.143:  52     c_stmts_opt ::= c_stmts (42)
L.143:  52     ifstmts_jumpc ::= c_stmts (42)
L.142:  28-78  iflaststmtc ::= testexpr c_stmts (42)
Reduce iflaststmtc invalid by check
L.142:  28-78  iflaststmtc ::= testexprc c_stmts (42)
Reduce iflaststmtc invalid by check
        40     c_stmts_opt ::= c_stmts (42)
        40     c_stmts_opt ::= c_stmts (42)
        40     ifstmts_jumpc ::= c_stmts (42)
L.142:  28     stmts ::= stmt (42)
L.142:  28     c_stmt ::= stmt (42)
L.142:  28     sstmt ::= stmt (42)
               stmts ::= stmts stmt (42)
L.142:  28-78  ifstmtc ::= testexpr ifstmts_jumpc (42)
Reduce ifstmtc invalid by check
L.142:  28-78  ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms (42)
Reduce ifstmtc invalid by check
L.142:  28-78  if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms (42)
Reduce if_not_stmtc invalid by check
L.142:  28     _stmts ::= stmts (42)
L.142:  28     c_stmts ::= c_stmt (42)
L.142:  28     stmts ::= sstmt (42)
               stmts ::= stmts sstmt (42)
               START ::= |- stmts (42)
               _stmts ::= stmts (42)
L.142:  28     c_stmts ::= _stmts (42)
L.142:  28     suite_stmts ::= _stmts (42)
L.142:  28     c_stmts ::= _stmts (42)
               c_stmts ::= _stmts (42)
L.142:  28     else_suite ::= suite_stmts (42)
               ifelsestmtc ::= testexpr c_stmts come_froms else_suite (42)
               lastc_stmt ::= ifelsestmtc (42)
Reduce lastc_stmt invalid by check
               c_stmt ::= ifelsestmtc (42)
               c_stmts ::= c_stmt (42)
        52-80  ifstmts_jump ::= COME_FROM stmts COME_FROM (43)
        80     come_froms ::= COME_FROM (43)
        80-80  _come_froms ::= \e__come_froms COME_FROM (43)
L.142:  28-80  if_or_stmt ::= expr POP_JUMP_IF_TRUE expr pop_jump come_froms stmts COME_FROM (43)
        80     come_froms ::= COME_FROM (43)
        80-80  _come_froms ::= \e__come_froms COME_FROM (43)
        80     come_froms ::= COME_FROM (43)
        80     come_from_opt ::= COME_FROM (43)
        80     come_froms ::= COME_FROM (43)
        40-80  ifstmt ::= testexpr ifstmts_jump \e__come_froms (43)
Reduce ifstmt invalid by check
        52     ifstmts_jumpc ::= ifstmts_jump (43)
L.142:  28-80  ifstmt ::= testexpr ifstmts_jump \e__come_froms (43)
        52-80  ifstmts_jump ::= COME_FROM stmts come_froms (43)
L.142:  28-80  ifstmt_bool ::= not_and_not stmts come_froms (43)
L.142:  28-80  ifstmt_bool ::= or_and1 stmts come_froms (43)
L.143:  52-80  ifstmts_jump ::= stmts come_froms (43)
L.143:  52-80  ifstmts_jump ::= stmts_opt come_froms (43)
        52-80  ifstmts_jumpc ::= COME_FROM c_stmts come_froms (43)
        28-80  whilestmt38 ::= _come_froms testexpr c_stmts come_froms (43)
Reduce whilestmt38 invalid by check
L.142:  28-80  whilestmt38 ::= \e__come_froms testexpr c_stmts come_froms (43)
Reduce whilestmt38 invalid by check
L.142:  28-80  iflaststmtc ::= testexpr c_stmts come_froms (43)
Reduce iflaststmtc invalid by check
L.142:  28-80  iflaststmtc ::= testexpr c_stmts come_froms (43)
Reduce iflaststmtc invalid by check
L.143:  52-80  ifstmts_jumpc ::= c_stmts_opt come_froms (43)
        40-80  ifstmts_jumpc ::= c_stmts_opt come_froms (43)
L.142:  28-80  ifstmt ::= testexpr stmts _come_froms (43)
L.142:  28-80  ifstmtc ::= testexprc ifstmts_jumpc _come_froms (43)
Reduce ifstmtc invalid by check
L.142:  28-80  if_not_stmtc ::= testexprc ifstmts_jumpc _come_froms (43)
Reduce if_not_stmtc invalid by check
L.142:  28     stmt ::= if_or_stmt (43)
        40-80  ifstmtc ::= testexpr ifstmts_jumpc (43)
Reduce ifstmtc invalid by check
        40-80  ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms (43)
Reduce ifstmtc invalid by check
        40-80  if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms (43)
Reduce if_not_stmtc invalid by check
L.142:  28-80  ifstmtc ::= testexpr ifstmts_jumpc (43)
Reduce ifstmtc invalid by check
L.142:  28-80  ifstmtc ::= testexprc ifstmts_jumpc \e__come_froms (43)
Reduce ifstmtc invalid by check
L.142:  28-80  if_not_stmtc ::= testexprc ifstmts_jumpc \e__come_froms (43)
Reduce if_not_stmtc invalid by check
L.142:  28     stmt ::= ifstmt (43)
L.142:  28     stmt ::= ifstmt_bool (43)
L.143:  52     ifstmts_jumpc ::= ifstmts_jump (43)
L.142:  28     stmts ::= stmt (43)
L.142:  28     c_stmt ::= stmt (43)
L.142:  28     sstmt ::= stmt (43)
               stmts ::= stmts stmt (43)
L.142:  28     _stmts ::= stmts (43)
L.142:  28     c_stmts ::= c_stmt (43)
               c_stmts ::= c_stmts c_stmt (43)
L.142:  28     stmts ::= sstmt (43)
               stmts ::= stmts sstmt (43)
               START ::= |- stmts (43)
               _stmts ::= stmts (43)
L.142:  28     c_stmts ::= _stmts (43)
L.142:  28     suite_stmts ::= _stmts (43)
L.142:  28     c_stmts ::= _stmts (43)
               c_stmts ::= _stmts (43)
L.142:  28     else_suite ::= suite_stmts (43)
               ifelsestmtc ::= testexpr c_stmts come_froms else_suite (43)
               lastc_stmt ::= ifelsestmtc (43)
Reduce lastc_stmt invalid by check
               c_stmt ::= ifelsestmtc (43)
               c_stmts ::= c_stmt (43)
L.147:  80     expr ::= LOAD_FAST (44)
L.147:  80     return_expr ::= expr (44)
L.147:  80     return_expr ::= expr (44)
L.147:  80-82  attribute ::= expr LOAD_ATTR (45)
L.147:  80     expr ::= attribute (45)
L.147:  80     return_expr ::= expr (45)
L.147:  80     return_expr ::= expr (45)
L.147:  80-84  attribute37 ::= expr LOAD_METHOD (46)
L.147:  80     expr ::= attribute37 (46)
L.147:  80     return_expr ::= expr (46)
L.147:  80     return_expr ::= expr (46)
L.147:  80-86  call ::= expr CALL_METHOD_0 (47)
L.147:  80     expr ::= call (47)
L.147:  80     return_expr ::= expr (47)
L.147:  80     return_expr ::= expr (47)
        88     store ::= STORE_FAST (48)
L.147:  80-88  assign ::= expr store (48)
L.147:  80     stmt ::= assign (48)
L.147:  80     stmts ::= stmt (48)
L.147:  80     c_stmt ::= stmt (48)
L.147:  80     sstmt ::= stmt (48)
L.142:  28-88  stmts ::= stmts stmt (48)
               stmts ::= stmts stmt (48)
L.147:  80     _stmts ::= stmts (48)
L.147:  80     c_stmts ::= c_stmt (48)
L.142:  28-88  c_stmts ::= c_stmts c_stmt (48)
               c_stmts ::= c_stmts c_stmt (48)
L.147:  80     stmts ::= sstmt (48)
L.142:  28-88  stmts ::= stmts sstmt (48)
               stmts ::= stmts sstmt (48)
L.142:  28     _stmts ::= stmts (48)
               START ::= |- stmts (48)
               _stmts ::= stmts (48)
L.147:  80     suite_stmts ::= _stmts (48)
L.147:  80     c_stmts ::= _stmts (48)
L.147:  80     c_stmts ::= _stmts (48)
L.142:  28     c_stmts ::= _stmts (48)
L.142:  28     suite_stmts ::= _stmts (48)
L.142:  28     c_stmts ::= _stmts (48)
               c_stmts ::= _stmts (48)
L.147:  80     else_suite ::= suite_stmts (48)
L.142:  28     else_suite ::= suite_stmts (48)
L.142:  28-88  ifelsestmtc ::= testexpr c_stmts come_froms else_suite (48)
               ifelsestmtc ::= testexpr c_stmts come_froms else_suite (48)
L.142:  28     lastc_stmt ::= ifelsestmtc (48)
Reduce lastc_stmt invalid by check
L.142:  28     c_stmt ::= ifelsestmtc (48)
L.142:  28     lastc_stmt ::= ifelsestmtc (48)
Reduce lastc_stmt invalid by check
               lastc_stmt ::= ifelsestmtc (48)
Reduce lastc_stmt invalid by check
               c_stmt ::= ifelsestmtc (48)
L.142:  28     c_stmts ::= c_stmt (48)
               c_stmts ::= c_stmt (48)
L.148:  90     expr ::= LOAD_FAST (49)
L.148:  90     return_expr ::= expr (49)
L.148:  90     return_expr ::= expr (49)
L.148:  90-92  attribute ::= expr LOAD_ATTR (50)
L.148:  90     expr ::= attribute (50)
L.148:  90     return_expr ::= expr (50)
L.148:  90     return_expr ::= expr (50)
L.148:  90-94  attribute37 ::= expr LOAD_METHOD (51)
L.148:  90     expr ::= attribute37 (51)
L.148:  90     return_expr ::= expr (51)
L.148:  90     return_expr ::= expr (51)
L.148:  90-96  call ::= expr CALL_METHOD_0 (52)
L.148:  90     expr ::= call (52)
L.148:  90     return_expr ::= expr (52)
L.148:  90     return_expr ::= expr (52)
L.148:  90-98  attribute37 ::= expr LOAD_METHOD (53)
L.148:  90     expr ::= attribute37 (53)
L.148:  90     return_expr ::= expr (53)
L.148:  90     return_expr ::= expr (53)
       100     expr ::= LOAD_FAST (54)
L.148:  90-102 call ::= expr expr CALL_METHOD_1 (55)
L.148:  90     expr ::= call (55)
L.148:  90     return_expr ::= expr (55)
L.148:  90     return_expr ::= expr (55)
       104     store ::= STORE_FAST (56)
L.148:  90-104 assign ::= expr store (56)
L.148:  90     stmt ::= assign (56)
L.147:  80-104 stmts ::= stmts stmt (56)
L.148:  90     stmts ::= stmt (56)
L.148:  90     c_stmt ::= stmt (56)
L.148:  90     sstmt ::= stmt (56)
L.142:  28-104 stmts ::= stmts stmt (56)
               stmts ::= stmts stmt (56)
L.147:  80     _stmts ::= stmts (56)
L.148:  90     _stmts ::= stmts (56)
L.148:  90     c_stmts ::= c_stmt (56)
L.147:  80-104 c_stmts ::= c_stmts c_stmt (56)
L.142:  28-104 c_stmts ::= c_stmts c_stmt (56)
               c_stmts ::= c_stmts c_stmt (56)
L.147:  80-104 stmts ::= stmts sstmt (56)
L.148:  90     stmts ::= sstmt (56)
L.142:  28-104 stmts ::= stmts sstmt (56)
               stmts ::= stmts sstmt (56)
L.142:  28     _stmts ::= stmts (56)
               START ::= |- stmts (56)
               _stmts ::= stmts (56)
L.147:  80     suite_stmts ::= _stmts (56)
L.147:  80     c_stmts ::= _stmts (56)
L.147:  80     c_stmts ::= _stmts (56)
L.148:  90     c_stmts ::= _stmts (56)
L.142:  28     c_stmts ::= _stmts (56)
L.142:  28     suite_stmts ::= _stmts (56)
L.142:  28     c_stmts ::= _stmts (56)
               c_stmts ::= _stmts (56)
L.147:  80     else_suite ::= suite_stmts (56)
L.142:  28     else_suite ::= suite_stmts (56)
L.142:  28-104 ifelsestmtc ::= testexpr c_stmts come_froms else_suite (56)
               ifelsestmtc ::= testexpr c_stmts come_froms else_suite (56)
L.142:  28     lastc_stmt ::= ifelsestmtc (56)
Reduce lastc_stmt invalid by check
L.142:  28     c_stmt ::= ifelsestmtc (56)
L.142:  28     lastc_stmt ::= ifelsestmtc (56)
Reduce lastc_stmt invalid by check
               lastc_stmt ::= ifelsestmtc (56)
Reduce lastc_stmt invalid by check
               c_stmt ::= ifelsestmtc (56)
L.142:  28     c_stmts ::= c_stmt (56)
               c_stmts ::= c_stmt (56)
L.149: 106     expr ::= LOAD_FAST (57)
L.149: 106     return_expr ::= expr (57)
L.149: 106     return_expr ::= expr (57)
L.149: 106-108 attribute37 ::= expr LOAD_METHOD (58)
L.149: 106     expr ::= attribute37 (58)
L.149: 106     return_expr ::= expr (58)
L.149: 106     return_expr ::= expr (58)
       110     expr ::= LOAD_FAST (59)
       112     expr ::= LOAD_FAST (60)
       112-114 attribute ::= expr LOAD_ATTR (61)
       112     expr ::= attribute (61)
L.149: 106-116 call ::= expr expr expr CALL_METHOD_2 (62)
L.149: 106     expr ::= call (62)
L.149: 106     return_expr ::= expr (62)
L.149: 106     return_expr ::= expr (62)
L.149: 106-118 expr_stmt ::= expr POP_TOP (63)
L.149: 106     stmt ::= expr_stmt (63)
L.147:  80-118 stmts ::= stmts stmt (63)
L.149: 106     stmts ::= stmt (63)
L.149: 106     c_stmt ::= stmt (63)
L.149: 106     sstmt ::= stmt (63)
L.148:  90-118 stmts ::= stmts stmt (63)
L.142:  28-118 stmts ::= stmts stmt (63)
               stmts ::= stmts stmt (63)
L.147:  80     _stmts ::= stmts (63)
L.149: 106     _stmts ::= stmts (63)
L.149: 106     c_stmts ::= c_stmt (63)
L.148:  90-118 c_stmts ::= c_stmts c_stmt (63)
L.147:  80-118 c_stmts ::= c_stmts c_stmt (63)
L.142:  28-118 c_stmts ::= c_stmts c_stmt (63)
               c_stmts ::= c_stmts c_stmt (63)
L.147:  80-118 stmts ::= stmts sstmt (63)
L.149: 106     stmts ::= sstmt (63)
L.148:  90-118 stmts ::= stmts sstmt (63)
L.142:  28-118 stmts ::= stmts sstmt (63)
               stmts ::= stmts sstmt (63)
L.148:  90     _stmts ::= stmts (63)
L.142:  28     _stmts ::= stmts (63)
               START ::= |- stmts (63)
               _stmts ::= stmts (63)
L.147:  80     suite_stmts ::= _stmts (63)
L.147:  80     c_stmts ::= _stmts (63)
L.147:  80     c_stmts ::= _stmts (63)
L.149: 106     c_stmts ::= _stmts (63)
L.148:  90     c_stmts ::= _stmts (63)
L.142:  28     c_stmts ::= _stmts (63)
L.142:  28     suite_stmts ::= _stmts (63)
L.142:  28     c_stmts ::= _stmts (63)
               c_stmts ::= _stmts (63)
L.147:  80     else_suite ::= suite_stmts (63)
L.142:  28     else_suite ::= suite_stmts (63)
L.142:  28-118 ifelsestmtc ::= testexpr c_stmts come_froms else_suite (63)
               ifelsestmtc ::= testexpr c_stmts come_froms else_suite (63)
L.142:  28     lastc_stmt ::= ifelsestmtc (63)
Reduce lastc_stmt invalid by check
L.142:  28     c_stmt ::= ifelsestmtc (63)
L.142:  28     lastc_stmt ::= ifelsestmtc (63)
Reduce lastc_stmt invalid by check
               lastc_stmt ::= ifelsestmtc (63)
Reduce lastc_stmt invalid by check
               c_stmt ::= ifelsestmtc (63)
L.142:  28     c_stmts ::= c_stmt (63)
               c_stmts ::= c_stmt (63)
L.150: 120     expr ::= LOAD_FAST (64)
L.150: 120     return_expr ::= expr (64)
L.150: 120     return_expr ::= expr (64)
       122     expr ::= LOAD_FAST (65)
       122-124 attribute ::= expr LOAD_ATTR (66)
       122     expr ::= attribute (66)
       126     binary_operator ::= BINARY_ADD (67)
L.150: 120-126 bin_op ::= expr expr binary_operator (67)
L.150: 120     expr ::= bin_op (67)
L.150: 120     return_expr ::= expr (67)
L.150: 120     return_expr ::= expr (67)
L.150: 120-128 return ::= return_expr RETURN_VALUE (68)
L.150: 120     stmt ::= return (68)
L.150: 120     returns ::= return (68)
L.147:  80-128 returns ::= _stmts return (68)
L.149: 106-128 returns ::= _stmts return (68)
L.149: 106-128 c_returns ::= c_stmts return (68)
L.148:  90-128 c_returns ::= c_stmts return (68)
L.147:  80-128 c_returns ::= c_stmts return (68)
L.142:  28-128 c_returns ::= c_stmts return (68)
               c_returns ::= c_stmts return (68)
L.148:  90-128 returns ::= _stmts return (68)
L.142:  28-128 returns ::= _stmts return (68)
               returns ::= _stmts return (68)
L.147:  80-128 stmts ::= stmts stmt (68)
L.150: 120     stmts ::= stmt (68)
L.150: 120     c_stmt ::= stmt (68)
L.150: 120     sstmt ::= stmt (68)
L.149: 106-128 stmts ::= stmts stmt (68)
L.148:  90-128 stmts ::= stmts stmt (68)
L.142:  28-128 stmts ::= stmts stmt (68)
               stmts ::= stmts stmt (68)
L.150: 120     c_returns ::= returns (68)
L.147:  80     else_suite ::= returns (68)
L.147:  80     suite_stmts ::= returns (68)
L.147:  80     c_returns ::= returns (68)
L.147:  80     c_returns ::= returns (68)
L.149: 106     c_returns ::= returns (68)
L.149: 106     c_stmts ::= c_returns (68)
L.148:  90     c_stmts ::= c_returns (68)
L.147:  80     c_stmts ::= c_returns (68)
L.142:  28     c_stmts ::= c_returns (68)
               c_stmts ::= c_returns (68)
L.148:  90     c_returns ::= returns (68)
L.142:  28     c_returns ::= returns (68)
L.142:  28     else_suite ::= returns (68)
L.142:  28     suite_stmts ::= returns (68)
L.142:  28     c_returns ::= returns (68)
               c_returns ::= returns (68)
L.147:  80     _stmts ::= stmts (68)
L.150: 120     _stmts ::= stmts (68)
L.150: 120     c_stmts ::= c_stmt (68)
L.149: 106-128 c_stmts ::= c_stmts c_stmt (68)
L.148:  90-128 c_stmts ::= c_stmts c_stmt (68)
L.147:  80-128 c_stmts ::= c_stmts c_stmt (68)
L.142:  28-128 c_stmts ::= c_stmts c_stmt (68)
               c_stmts ::= c_stmts c_stmt (68)
L.147:  80-128 stmts ::= stmts sstmt (68)
L.150: 120     stmts ::= sstmt (68)
L.149: 106-128 stmts ::= stmts sstmt (68)
L.148:  90-128 stmts ::= stmts sstmt (68)
L.142:  28-128 stmts ::= stmts sstmt (68)
               stmts ::= stmts sstmt (68)
L.149: 106     _stmts ::= stmts (68)
L.148:  90     _stmts ::= stmts (68)
L.142:  28     _stmts ::= stmts (68)
               START ::= |- stmts (68)
               _stmts ::= stmts (68)
L.150: 120     c_stmts ::= c_returns (68)
L.142:  28-128 ifelsestmtc ::= testexpr c_stmts come_froms else_suite (68)
L.147:  80     else_suite ::= suite_stmts (68)
               ifelsestmtc ::= testexpr c_stmts come_froms else_suite (68)
L.142:  28     else_suite ::= suite_stmts (68)
L.147:  80     suite_stmts ::= _stmts (68)
L.147:  80     c_stmts ::= _stmts (68)
L.147:  80     c_stmts ::= _stmts (68)
L.150: 120     c_stmts ::= _stmts (68)
L.149: 106     c_stmts ::= _stmts (68)
L.148:  90     c_stmts ::= _stmts (68)
L.142:  28     c_stmts ::= _stmts (68)
L.142:  28     suite_stmts ::= _stmts (68)
L.142:  28     c_stmts ::= _stmts (68)
               c_stmts ::= _stmts (68)
L.142:  28     lastc_stmt ::= ifelsestmtc (68)
Reduce lastc_stmt invalid by check
L.142:  28     c_stmt ::= ifelsestmtc (68)
L.142:  28     lastc_stmt ::= ifelsestmtc (68)
Reduce lastc_stmt invalid by check
               lastc_stmt ::= ifelsestmtc (68)
Reduce lastc_stmt invalid by check
               c_stmt ::= ifelsestmtc (68)
L.142:  28     c_stmts ::= c_stmt (68)
               c_stmts ::= c_stmt (68)
               sstmt ::= return RETURN_LAST (69)
               sstmt ::= sstmt RETURN_LAST (69)
               stmts ::= stmts sstmt (69)
               stmts ::= sstmt (69)
               stmts ::= stmts sstmt (69)
               stmts ::= stmts sstmt (69)
               stmts ::= stmts sstmt (69)
               stmts ::= stmts sstmt (69)
               _stmts ::= stmts (69)
               _stmts ::= stmts (69)
               _stmts ::= stmts (69)
               _stmts ::= stmts (69)
               _stmts ::= stmts (69)
               START ::= |- stmts (69)
               _stmts ::= stmts (69)
               suite_stmts ::= _stmts (69)
               c_stmts ::= _stmts (69)
               c_stmts ::= _stmts (69)
               c_stmts ::= _stmts (69)
               c_stmts ::= _stmts (69)
               c_stmts ::= _stmts (69)
               c_stmts ::= _stmts (69)
               suite_stmts ::= _stmts (69)
               c_stmts ::= _stmts (69)
               c_stmts ::= _stmts (69)
               else_suite ::= suite_stmts (69)
               else_suite ::= suite_stmts (69)
               ifelsestmtc ::= testexpr c_stmts come_froms else_suite (69)
               ifelsestmtc ::= testexpr c_stmts come_froms else_suite (69)
L.142:  28     lastc_stmt ::= ifelsestmtc (69)
Reduce lastc_stmt invalid by check
L.142:  28     c_stmt ::= ifelsestmtc (69)
L.142:  28     lastc_stmt ::= ifelsestmtc (69)
Reduce lastc_stmt invalid by check
               lastc_stmt ::= ifelsestmtc (69)
Reduce lastc_stmt invalid by check
               c_stmt ::= ifelsestmtc (69)
L.142:  28     c_stmts ::= c_stmt (69)
               c_stmts ::= c_stmts c_stmt (69)
               c_stmts ::= c_stmt (69)
               expr ::= LOAD_GLOBAL (1)
               return_expr ::= expr (1)
         2     expr ::= LOAD_FAST (2)
         2-4   attribute ::= expr LOAD_ATTR (3)
         2     expr ::= attribute (3)
         6     expr ::= LOAD_CONST (4)
               call ::= expr expr expr CALL_FUNCTION_2 (5)
               expr ::= call (5)
               return_expr ::= expr (5)
L.155:  10     expr ::= LOAD_FAST (6)
L.155:  10-12  attribute ::= expr LOAD_ATTR (7)
L.155:  10     expr ::= attribute (7)
L.153:  14     expr ::= LOAD_CONST (8)
               dict ::= expr expr LOAD_CONST BUILD_CONST_KEY_MAP_2 (9)
               expr ::= dict (9)
               return_expr ::= expr (9)
               return ::= return_expr RETURN_VALUE (10)
               stmt ::= return (10)
               returns ::= return (10)
               stmts ::= stmt (10)
               sstmt ::= stmt (10)
               c_stmt ::= stmt (10)
               c_returns ::= returns (10)
               START ::= |- stmts (10)
               _stmts ::= stmts (10)
               stmts ::= sstmt (10)
               c_stmts ::= c_stmt (10)
               c_stmts ::= c_returns (10)
               c_stmts ::= _stmts (10)
               sstmt ::= return RETURN_LAST (11)
               sstmt ::= sstmt RETURN_LAST (11)
               stmts ::= sstmt (11)
               START ::= |- stmts (11)
               _stmts ::= stmts (11)
               c_stmts ::= _stmts (11)
               expr ::= LOAD_FAST (1)
               return_expr ::= expr (1)
               attribute37 ::= expr LOAD_METHOD (2)
               expr ::= attribute37 (2)
               return_expr ::= expr (2)
               call ::= expr CALL_METHOD_0 (3)
               expr ::= call (3)
               return_expr ::= expr (3)
               attribute37 ::= expr LOAD_METHOD (4)
               expr ::= attribute37 (4)
               return_expr ::= expr (4)
         8     expr ::= LOAD_STR (5)
               call ::= expr expr CALL_METHOD_1 (6)
               expr ::= call (6)
               return_expr ::= expr (6)
        12     store ::= STORE_FAST (7)
               assign ::= expr store (7)
               stmt ::= assign (7)
               stmts ::= stmt (7)
               sstmt ::= stmt (7)
               c_stmt ::= stmt (7)
               START ::= |- stmts (7)
               _stmts ::= stmts (7)
               stmts ::= sstmt (7)
               c_stmts ::= c_stmt (7)
               c_stmts ::= _stmts (7)
L.162:  14     expr ::= LOAD_FAST (8)
L.162:  14     return_expr ::= expr (8)
L.162:  14     return_expr ::= expr (8)
L.162:  14-16  attribute37 ::= expr LOAD_METHOD (9)
L.162:  14     expr ::= attribute37 (9)
L.162:  14     return_expr ::= expr (9)
L.162:  14     return_expr ::= expr (9)
        18     expr ::= LOAD_STR (10)
        20     expr ::= LOAD_GLOBAL (11)
L.162:  14-22  call ::= expr expr expr CALL_METHOD_2 (12)
L.162:  14     expr ::= call (12)
L.162:  14     return_expr ::= expr (12)
L.162:  14     return_expr ::= expr (12)
               expr_stmt ::= expr POP_TOP (13)
               stmt ::= expr_stmt (13)
               stmts ::= stmts stmt (13)
               stmts ::= stmt (13)
               sstmt ::= stmt (13)
               c_stmt ::= stmt (13)
               START ::= |- stmts (13)
               _stmts ::= stmts (13)
               _stmts ::= stmts (13)
               stmts ::= stmts sstmt (13)
               stmts ::= sstmt (13)
               c_stmts ::= c_stmt (13)
               c_stmts ::= c_stmts c_stmt (13)
               c_stmts ::= _stmts (13)
               c_stmts ::= _stmts (13)
import logging
from . import bus
AHT10_I2C_ADDR = 56
AHT10_COMMANDS = {'INIT':[
  225, 8, 0], 
 'MEASURE':[
  172, 51, 0], 
 'RESET':[
  186, 8, 0]}
AHT10_MAX_BUSY_CYCLES = 5

class AHT10:

    def __init__(self, config):
        self.printer = config.get_printer()
        self.name = config.get_name().split()[-1]
        self.reactor = self.printer.get_reactor()
        self.i2c = bus.MCU_I2C_from_config(config,
          default_addr=AHT10_I2C_ADDR, default_speed=100000)
        self.report_time = config.getint("aht10_report_time", 30, minval=5)
        self.temp = self.min_temp = self.max_temp = self.humidity = 0.0
        self.sample_timer = self.reactor.register_timer(self._sample_aht10)
        self.printer.add_object("aht10 " + self.name, self)
        self.printer.register_event_handler("klippy:connect", self.handle_connect)
        self.is_calibrated = False
        self.init_sent = False

    def handle_connect(self):
        self._init_aht10()
        self.reactor.update_timer(self.sample_timer, self.reactor.NOW)

    def setup_minmax(self, min_temp, max_temp):
        self.min_temp = min_temp
        self.max_temp = max_temp

    def setup_callback(self, cb):
        self._callback = cb

    def get_report_time_delta(self):
        return self.report_time

    def _make_measurementParse error at or near `LOAD_FAST' instruction at offset 0

    def _reset_device(self):
        if not self.init_sent:
            return
        self.i2c.i2c_write(AHT10_COMMANDS["RESET"])
        self.reactor.pause(self.reactor.monotonic() + 0.1)

    def _init_aht10(self):
        self.i2c.i2c_write(AHT10_COMMANDS["INIT"])
        self.reactor.pause(self.reactor.monotonic() + 0.1)
        self.init_sent = True
        if self._make_measurement():
            logging.info("aht10: successfully initialized, initial temp: " + "%.3f, humidity: %.3f" % (self.temp, self.humidity))

    def _sample_aht10(self, eventtime):
        if not self._make_measurement():
            self.temp = self.humidity = 0.0
            return self.reactor.NEVER
        if self.temp < self.min_temp or self.temp > self.max_temp:
            self.printer.invoke_shutdown("AHT10 temperature %0.1f outside range of %0.1f:%.01f" % (
             self.temp, self.min_temp, self.max_temp))
        measured_time = self.reactor.monotonic()
        print_time = self.i2c.get_mcu().estimated_print_time(measured_time)
        self._callback(print_time, self.temp)
        return measured_time + self.report_time

    def get_status(self, eventtime):
        return {'temperature':round(self.temp, 2), 
         'humidity':self.humidity}


def load_config(config):
    pheater = config.get_printer().lookup_object("heaters")
    pheater.add_sensor_factory("AHT10", AHT10)
