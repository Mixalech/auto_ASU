from telegram import InlineKeyboardButton


###level -1
kb_start = [
        [
            InlineKeyboardButton("🗂 Полезная Информация", callback_data="start_info")
        ],
        [
            InlineKeyboardButton("🔎 Задать вопрос", callback_data="start_question")
        ]
    ]

###level 0
kb_info = [
    [
        InlineKeyboardButton("🧩 Внеучебная деятельность", callback_data="info_activities")
    ],
    [
        InlineKeyboardButton("📌 Справочник студента", callback_data="info_student")
    ],
    [
        InlineKeyboardButton("⬅️ Назад", callback_data="start_call")
    ],
]

kb_feedback = [
    [
        InlineKeyboardButton("🚫 Не хочу задавать вопрос", callback_data="question_stop")
    ]
]

###level 1
kb_answer = [
    [
        InlineKeyboardButton("✅ Правильный ответ", callback_data="answer_correct")
    ],
    [
        InlineKeyboardButton("❌ Неправильный/неполный ответ", callback_data="answer_uncorrect")
    ]
]

kb_student = [
    [
        InlineKeyboardButton("⏱ Учебный процесс", callback_data="student_study")
    ],
    [
        InlineKeyboardButton("🪖 Военнообязаным", callback_data="student_army"),
        InlineKeyboardButton("🔑 Общежитие", callback_data="student_home")
    ],
    [
        InlineKeyboardButton("☎️ Контактная информация", callback_data="student_contact")
    ],
    [
        InlineKeyboardButton("⬅️ Назад", callback_data="start_info")
    ],
]



kb_activities = [
        [
            InlineKeyboardButton("👀 Студенческая Администрация 👥", callback_data="activities_SA")
        ],
        [
            InlineKeyboardButton("🎥 Медиацентр 📸", callback_data="activities_media"),
            InlineKeyboardButton("🎯 Кружковые объединения", callback_data="activities_another")
        ],
        [
            InlineKeyboardButton("⬅️ Назад", callback_data="start_info")
        ],
    ]

###level 2
kb_media = [
    [
        InlineKeyboardButton("⬅️ Назад", callback_data="info_activities")
    ]
]

kb_stud = [
    [
        InlineKeyboardButton("⬅️ Назад", callback_data="info_student")
    ]
]

kb_contact = [
    [
        InlineKeyboardButton("🖥 ЭиИТ", callback_data="contact_it")
    ],
    [
        InlineKeyboardButton("⚖️ ГУМ", callback_data="contact_gum")
    ],
    [
        InlineKeyboardButton("⚗️ ПСиТ", callback_data="contact_psit")
    ],
    [
        InlineKeyboardButton("⬅️ Назад", callback_data="info_student")
    ],
]

kb_study = [
    [
        InlineKeyboardButton("🏫 Учебные корпуса", callback_data="study_korpus")
    ],
    [
        InlineKeyboardButton("📋 Тех.карты", callback_data="study_map")
    ], 
    [
        InlineKeyboardButton("⬅️ Назад", callback_data="info_student")
    ],
]

kb_SA = [
    [
        InlineKeyboardButton("🎉 Культорги", callback_data="SA_cultorg"),
        InlineKeyboardButton("🏆 Спорторги", callback_data="SA_sportorg")
    ],
    [
        InlineKeyboardButton("📰 СНО", callback_data="SA_SNO"),
    ],
    [
        InlineKeyboardButton("⬅️ Назад", callback_data="info_activities")
    ],
]

kb_another = [
    [
        InlineKeyboardButton("⛑ Волонтерский отряд «Бумеранг»", callback_data="another_volonter"),
    ],
    [
        InlineKeyboardButton("💻 Научное объединение «Технология дополненной и виртуальной реальности 2.0»", callback_data="another_VIAR"),
    ],
    [
        InlineKeyboardButton("💰 Клуб «Финансист»", callback_data="another_finans"),
    ],
    [
        InlineKeyboardButton("🎲 Клуб по интересам «Настольные игры»", callback_data="another_games")
    ],
    [
        InlineKeyboardButton("♟ Клуб «Математические шахматы»", callback_data="another_mathchess"),
    ],
    [
        InlineKeyboardButton("🎭 Театральная студия Колледжа АлтГУ", callback_data="another_theatre")
    ],
    [
        InlineKeyboardButton("⛹️ Спортивные секции: волейбол и баскетбол 🏐", callback_data="another_sport")
    ],
    [
        InlineKeyboardButton("🧮 Центр содействия развития предпринимательства «Ориентир»", callback_data="another_bisness")
    ],
    [
        InlineKeyboardButton("🪖 Военно-патриотической клуб «Струна»", callback_data="another_struna")
    ],
    [
        InlineKeyboardButton("🛡 Народная дружина «СтудГвардия»", callback_data="another_druzina")
    ],
    [
        InlineKeyboardButton("🏹 Стрелковый клуб «Ворошиловский стрелок»", callback_data="another_strelok")
    ],
    [
        InlineKeyboardButton("📺 Клуб исторической реконструкции", callback_data="another_reconstruct")
    ],
    [
        InlineKeyboardButton("🧳 Клуб спортивного туризма (пешеходный и водный)", callback_data="another_turism")
    ],
    [
        InlineKeyboardButton("🪆 Клуб любителей истории отечества (КЛИО)", callback_data="another_historyclub")
    ],
    [
        InlineKeyboardButton("⚖️ Кружковое объединение «Теория и история государства и права»", callback_data="another_pravo")
    ],
    [
        InlineKeyboardButton("🛎 Кружок «Секреты отельера»", callback_data="another_hotel")
    ],
    [
        InlineKeyboardButton("⬅️ Назад", callback_data="info_activities")
    ],
]

###level 3
kb_another_activ = [
    [
        InlineKeyboardButton("⬅️ Назад", callback_data="activities_another")
    ]
]

kb_SA_activ = [
    [
        InlineKeyboardButton("⬅️ Назад", callback_data="activities_SA")
    ]
]

kb_ycheb = [
    [
        InlineKeyboardButton("⬅️ Назад", callback_data="student_study")
    ]
]

kb_korp_contact = [
    [
        InlineKeyboardButton("⬅️ Назад", callback_data="student_contact")
    ]
]

kb_stop_question = [
    [
        InlineKeyboardButton("⬅️ Назад", callback_data="start_call")
    ]
]

kb_oper = [
    [
        InlineKeyboardButton("Следующий вопрос", callback_data="next_question")
    ]
]