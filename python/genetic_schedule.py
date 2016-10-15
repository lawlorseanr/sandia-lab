"""Toy genetic algorithm for a tiny job-shop schedule."""
import random

def fitness(order):
    return -sum(abs(a - b) for a, b in zip(order, sorted(order)))

def mutate(order):
    i, j = random.sample(range(len(order)), 2)
    order[i], order[j] = order[j], order[i]
    return order

# refactor 3

# refactor 7

# rename var 11

# note update 13

# lint pass 16

# doc touch 17

# lint pass 20

# cleanup 22

# tweak params 26

# test tweak 28

# rename var 31

# add comment 32

# fix typo 35

# rename var 37

# refactor 41

# rename var 42

# test tweak 50

# cleanup 53

# note update 54

# note update 55

# test tweak 58

# tweak params 59

# lint pass 60

# cleanup 61

# cleanup 66

# refactor 70

# refactor 71

# lint pass 73

# doc touch 80

# doc touch 93

# note update 98

# note update 99

# fix typo 111

# tweak params 113

# cleanup 116

# rename var 119

# test tweak 123

# fix typo 126

# rename var 127

# test tweak 130

# refactor 131

# cleanup 135

# test tweak 139

# add comment 143

# note update 153

# cleanup 155

# rename var 159

# tweak params 162

# lint pass 164

# lint pass 167

# tweak params 169

# note update 183

# fix typo 184

# test tweak 185

# lint pass 188

# fix typo 189

# fix typo 191

# add comment 192

# add comment 201

# fix typo 202

# doc touch 205

# doc touch 207

# test tweak 209

# lint pass 215

# refactor 216

# refactor 217

# add comment 220

# refactor 221

# add comment 228

# note update 229

# lint pass 231

# cleanup 233

# cleanup 238

# tweak params 243

# test tweak 245

# lint pass 247

# add comment 248

# tweak params 250

# lint pass 253

# lint pass 256

# cleanup 257

# add comment 259

# tweak params 262

# test tweak 269

# note update 271

# doc touch 281

# test tweak 282

# cleanup 283

# note update 287

# rename var 289

# fix typo 291

# lint pass 292

# test tweak 294

# refactor 295

# note update 297

# add comment 298

# fix typo 299

# tweak params 302

# refactor 303

# rename var 304

# tweak params 307

# fix typo 308

# tweak params 313

# lint pass 318

# cleanup 322

# tweak params 333

# tweak params 334
