use leetcode;
/* drop table Logs;
create table Logs (
    Id integer,
    Num integer
    );

insert into Logs (Id, Num) values 
(0,38),
(1,38),
(3,14),
(4,14),
(6,13),
(7,13),
(9,8),
(10,8),
(12,6),
(13,6),
(15,23),
(16,23),
(18,1),
(19,1),
(21,38),
(22,38),
(24,39),
(25,39),
(26,39),
(27,49),
(28,49),
(30,23),
(31,23),
(33,10),
(34,10),
(36,42),
(37,42),
(39,21),
(40,21),
(42,9),
(43,9),
(45,32),
(46,32),
(47,32),
(48,37),
(49,37),
(51,42),
(52,42),
(53,42),
(54,8),
(55,8),
(56,8),
(57,17),
(58,17),
(60,11),
(61,11),
(62,11),
(63,2),
(64,2),
(66,15),
(67,15),
(69,7),
(70,7),
(72,49),
(73,49),
(75,23),
(76,23),
(78,33),
(79,33),
(81,32),
(82,32),
(83,32),
(84,0),
(85,0),
(87,17),
(88,17),
(89,17),
(90,37),
(91,37),
(93,18),
(94,18),
(96,26),
(97,26),
(99,26),
(100,26),
(102,13),
(103,13),
(105,0),
(106,0),
(107,0),
(108,47),
(109,47),
(111,37),
(112,37),
(114,47),
(115,47),
(117,15),
(118,15),
(119,15),
(120,12),
(121,12),
(123,44),
(124,44),
(125,44),
(126,14),
(127,14),
(129,46),
(130,46),
(132,7),
(133,7),
(135,14),
(136,14),
(138,30),
(139,30),
(141,13),
(142,13),
(144,0),
(145,0),
(147,47),
(148,47),
(150,16),
(151,16),
(153,38),
(154,38),
(156,23),
(157,23),
(158,23),
(159,33),
(160,33),
(162,47),
(163,47),
(165,32),
(166,32),
(168,27),
(169,27),
(170,27),
(171,25),
(172,25),
(174,41),
(175,41),
(177,36),
(178,36),
(180,38),
(181,38),
(183,4),
(184,4),
(186,17),
(187,17),
(189,27),
(190,27),
(192,28),
(193,28),
(195,48),
(196,48),
(198,15),
(199,15),
(201,24),
(202,24),
(204,12),
(205,12),
(207,35),
(208,35),
(210,38),
(211,38),
(212,38),
(213,18),
(214,18),
(216,38),
(217,38),
(219,25),
(220,25),
(222,21),
(223,21),
(225,25),
(226,25),
(227,25),
(228,19),
(229,19),
(231,36),
(232,36),
(233,36),
(234,1),
(235,1),
(237,11),
(238,11),
(240,35),
(241,35),
(242,35),
(243,35),
(244,35),
(246,3),
(247,3),
(249,16),
(250,16),
(252,7),
(253,7),
(254,7),
(255,1),
(256,1),
(257,1),
(258,25),
(259,25),
(261,14),
(262,14),
(264,45),
(265,45),
(266,45),
(267,43),
(268,43),
(270,27),
(271,27),
(273,4),
(274,4),
(276,32),
(277,32),
(279,23),
(280,23),
(282,39),
(283,39),
(285,33),
(286,33),
(288,31),
(289,31),
(291,15),
(292,15),
(294,32),
(295,32),
(297,15),
(298,15),
(300,23),
(301,23),
(303,0),
(304,0),
(306,26),
(307,26),
(309,44),
(310,44),
(312,43),
(313,43),
(315,39),
(316,39),
(318,23),
(319,23),
(320,23),
(321,34),
(322,34),
(324,3),
(325,3),
(327,1),
(328,1),
(330,32),
(331,32),
(333,4),
(334,4),
(335,4),
(336,18),
(337,18),
(338,18),
(339,18),
(340,18),
(341,18),
(342,21),
(343,21),
(345,19),
(346,19),
(348,25),
(349,25),
(350,25),
(351,45),
(352,45),
(354,9),
(355,9),
(357,35),
(358,35),
(360,7),
(361,7),
(363,43),
(364,43),
(366,46),
(367,46),
(369,44),
(370,44),
(372,2),
(373,2),
(375,28),
(376,28),
(378,35),
(379,35),
(381,20),
(382,20),
(383,20),
(384,42),
(385,42),
(387,39),
(388,39),
(390,5),
(391,5),
(393,8),
(394,8),
(396,41),
(397,41),
(399,8),
(400,8),
(402,19),
(403,19),
(405,48),
(406,48),
(408,45),
(409,45),
(411,44),
(412,44),
(414,23),
(415,23),
(416,23),
(417,1),
(418,1),
(420,43),
(421,43),
(423,44),
(424,44),
(426,19),
(427,19),
(429,11),
(430,11),
(431,11),
(432,42),
(433,42),
(435,37),
(436,37),
(438,31),
(439,31),
(441,20),
(442,20),
(444,14),
(445,14),
(446,14),
(447,50),
(448,50),
(450,44),
(451,44),
(453,36),
(454,36),
(456,24),
(457,24),
(458,24),
(459,34),
(460,34),
(462,25),
(463,25),
(465,16),
(466,16),
(468,17),
(469,17),
(470,17),
(471,27),
(472,27),
(474,13),
(475,13),
(477,18),
(478,18),
(480,25),
(481,25),
(483,31),
(484,31),
(485,31),
(486,30),
(487,30),
(488,30),
(489,5),
(490,5),
(492,47),
(493,47),
(494,47),
(495,6),
(496,6),
(498,47),
(499,47),
(501,28),
(502,28),
(504,27),
(505,27),
(507,4),
(508,4),
(509,4),
(510,42),
(511,42),
(513,35),
(514,35),
(516,47),
(517,47),
(519,38),
(520,38),
(521,38),
(522,22),
(523,22),
(525,38),
(526,38),
(527,38),
(528,30),
(529,30),
(530,30),
(531,31),
(532,31),
(534,2),
(535,2),
(536,2),
(537,26),
(538,26),
(539,26),
(540,44),
(541,44),
(543,13),
(544,13),
(546,6),
(547,6),
(548,6),
(549,37),
(550,37),
(552,4),
(553,4),
(555,41),
(556,41),
(558,8),
(559,8),
(560,8),
(561,48),
(562,48),
(564,6),
(565,6),
(567,21),
(568,21),
(570,27),
(571,27),
(573,24),
(574,24),
(575,24),
(576,29),
(577,29),
(579,14),
(580,14),
(581,14),
(582,5),
(583,5),
(584,5),
(585,5),
(586,5),
(588,33),
(589,33),
(590,33),
(591,37),
(592,37),
(594,45),
(595,45),
(597,19),
(598,19),
(600,9),
(601,9),
(603,17),
(604,17),
(606,36),
(607,36),
(609,26),
(610,26),
(612,38),
(613,38),
(615,39),
(616,39),
(618,41),
(619,41),
(621,16),
(622,16),
(624,1),
(625,1),
(626,1),
(627,23),
(628,23),
(630,25),
(631,25),
(632,25),
(633,40),
(634,40),
(636,24),
(637,24),
(639,25),
(640,25),
(642,41),
(643,41),
(644,41),
(645,16),
(646,16),
(647,16),
(648,48),
(649,48),
(650,48),
(651,7),
(652,7),
(654,44),
(655,44),
(657,15),
(658,15),
(660,43),
(661,43),
(663,29),
(664,29),
(666,27),
(667,27),
(669,27),
(670,27),
(672,33),
(673,33),
(674,33),
(675,25),
(676,25),
(678,17),
(679,17),
(680,17),
(681,2),
(682,2),
(684,11),
(685,11),
(687,29),
(688,29),
(689,29),
(690,28),
(691,28),
(693,22),
(694,22),
(696,42),
(697,42),
(698,42),
(699,47),
(700,47),
(701,47),
(702,31),
(703,31),
(705,38),
(706,38),
(708,31),
(709,31),
(710,31),
(711,39),
(712,39),
(714,33),
(715,33),
(717,43),
(718,43),
(720,42),
(721,42),
(723,31),
(724,31),
(725,31),
(726,32),
(727,32),
(728,32),
(729,20),
(730,20),
(732,9),
(733,9),
(735,49),
(736,49),
(738,24),
(739,24),
(741,47),
(742,47),
(744,9),
(745,9),
(747,3),
(748,3),
(750,17),
(751,17),
(753,35),
(754,35),
(756,26),
(757,26),
(759,30),
(760,30),
(762,33),
(763,33),
(765,42),
(766,42),
(768,1),
(769,1),
(771,26),
(772,26),
(773,26),
(774,31),
(775,31),
(776,31),
(777,17),
(778,17),
(780,38),
(781,38),
(782,38),
(783,43),
(784,43),
(786,30),
(787,30),
(789,0),
(790,0),
(791,0),
(792,22),
(793,22),
(794,22),
(795,43),
(796,43),
(797,43),
(798,4),
(799,4),
(801,4),
(802,4),
(804,42),
(805,42),
(806,42),
(807,19),
(808,19),
(810,45),
(811,45),
(813,4),
(814,4),
(816,15),
(817,15),
(819,12),
(820,12),
(822,20),
(823,20),
(825,29),
(826,29),
(828,10),
(829,10),
(831,4),
(832,4),
(834,47),
(835,47),
(837,3),
(838,3),
(840,10),
(841,10),
(843,45),
(844,45),
(846,40),
(847,40),
(849,5),
(850,5),
(851,5),
(852,20),
(853,20),
(854,20),
(855,30),
(856,30),
(857,30),
(858,3),
(859,3),
(861,50),
(862,50),
(864,32),
(865,32),
(867,39),
(868,39),
(870,12),
(871,12),
(873,36),
(874,36),
(876,30),
(877,30),
(878,30),
(879,15),
(880,15),
(881,15),
(882,33),
(883,33),
(885,36),
(886,36),
(888,2),
(889,2),
(891,13),
(892,13),
(893,13),
(894,42),
(895,42),
(897,35),
(898,35)
;*/
-- select * from Logs;
-- select distinct a.Num ConsecutiveNums from Logs a left join Logs b on a.Id+1=b.Id left join Logs c on a.Id+2=c.Id where a.Num=b.Num and a.Num=c.Num;
select distinct a.Num ConsecutiveNums from Logs a, Logs b, Logs c where a.Id+1=b.Id and a.Id+2=c.Id and a.Num=b.Num and a.Num=c.Num;
-- select distinct a.Num ConsecutiveNums from Logs a left join Logs b on (a.Id+1=b.Id and a.Num=b.Num) left join Logs c on (a.Id+2=c.Id and a.Num=c.Num)
