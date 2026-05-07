---
title: Introduced vs Exposed Map
status: candidate / not-authority
authority: not-authority
---

# Introduced vs Exposed Map

Counts: `{'introduced': 54, 'exposed': 19, 'both': 7}`

| PR | introduced/exposed | rationale |
|---:|---|---|
| #1 | introduced | new candidate/contract/surface introduced |
| #161 | introduced | new candidate/contract/surface introduced |
| #162 | introduced | new candidate/contract/surface introduced |
| #163 | introduced | new candidate/contract/surface introduced |
| #164 | introduced | new candidate/contract/surface introduced |
| #165 | introduced | new candidate/contract/surface introduced |
| #166 | introduced | new candidate/contract/surface introduced |
| #167 | introduced | new candidate/contract/surface introduced |
| #168 | introduced | new candidate/contract/surface introduced |
| #169 | introduced | new candidate/contract/surface introduced |
| #170 | introduced | new candidate/contract/surface introduced |
| #171 | exposed | audit/readback/receipt/amendment exposed or narrowed existing truth |
| #172 | introduced | new candidate/contract/surface introduced |
| #173 | introduced | new candidate/contract/surface introduced |
| #174 | introduced | new candidate/contract/surface introduced |
| #175 | introduced | new candidate/contract/surface introduced |
| #176 | exposed | audit/readback/receipt/amendment exposed or narrowed existing truth |
| #177 | introduced | new candidate/contract/surface introduced |
| #178 | introduced | new candidate/contract/surface introduced |
| #179 | introduced | new candidate/contract/surface introduced |
| #180 | introduced | new candidate/contract/surface introduced |
| #181 | introduced | new candidate/contract/surface introduced |
| #182 | introduced | new candidate/contract/surface introduced |
| #183 | introduced | new candidate/contract/surface introduced |
| #184 | introduced | new candidate/contract/surface introduced |
| #185 | introduced | new candidate/contract/surface introduced |
| #186 | introduced | new candidate/contract/surface introduced |
| #187 | introduced | new candidate/contract/surface introduced |
| #188 | introduced | new candidate/contract/surface introduced |
| #189 | exposed | audit/readback/receipt/amendment exposed or narrowed existing truth |
| #190 | introduced | new candidate/contract/surface introduced |
| #191 | introduced | new candidate/contract/surface introduced |
| #192 | introduced | new candidate/contract/surface introduced |
| #193 | exposed | audit/readback/receipt/amendment exposed or narrowed existing truth |
| #194 | introduced | new candidate/contract/surface introduced |
| #195 | exposed | audit/readback/receipt/amendment exposed or narrowed existing truth |
| #196 | introduced | new candidate/contract/surface introduced |
| #197 | introduced | new candidate/contract/surface introduced |
| #198 | exposed | audit/readback/receipt/amendment exposed or narrowed existing truth |
| #199 | exposed | audit/readback/receipt/amendment exposed or narrowed existing truth |
| #200 | introduced | new candidate/contract/surface introduced |
| #201 | introduced | new candidate/contract/surface introduced |
| #202 | introduced | new candidate/contract/surface introduced |
| #203 | introduced | new candidate/contract/surface introduced |
| #204 | both | implementation introduced a seam and later amendment/readback exposed caveats |
| #205 | both | implementation introduced a seam and later amendment/readback exposed caveats |
| #206 | both | implementation introduced a seam and later amendment/readback exposed caveats |
| #207 | introduced | new candidate/contract/surface introduced |
| #208 | introduced | new candidate/contract/surface introduced |
| #209 | introduced | new candidate/contract/surface introduced |
| #210 | introduced | new candidate/contract/surface introduced |
| #211 | introduced | new candidate/contract/surface introduced |
| #212 | introduced | new candidate/contract/surface introduced |
| #213 | introduced | new candidate/contract/surface introduced |
| #214 | exposed | audit/readback/receipt/amendment exposed or narrowed existing truth |
| #215 | introduced | new candidate/contract/surface introduced |
| #216 | both | implementation introduced a seam and later amendment/readback exposed caveats |
| #217 | introduced | new candidate/contract/surface introduced |
| #218 | introduced | new candidate/contract/surface introduced |
| #219 | introduced | new candidate/contract/surface introduced |
| #220 | introduced | new candidate/contract/surface introduced |
| #221 | exposed | audit/readback/receipt/amendment exposed or narrowed existing truth |
| #222 | introduced | new candidate/contract/surface introduced |
| #223 | introduced | new candidate/contract/surface introduced |
| #224 | introduced | new candidate/contract/surface introduced |
| #225 | exposed | audit/readback/receipt/amendment exposed or narrowed existing truth |
| #226 | both | implementation introduced a seam and later amendment/readback exposed caveats |
| #227 | introduced | new candidate/contract/surface introduced |
| #228 | both | implementation introduced a seam and later amendment/readback exposed caveats |
| #230 | introduced | new candidate/contract/surface introduced |
| #231 | exposed | audit/readback/receipt/amendment exposed or narrowed existing truth |
| #232 | exposed | audit/readback/receipt/amendment exposed or narrowed existing truth |
| #233 | exposed | audit/readback/receipt/amendment exposed or narrowed existing truth |
| #234 | exposed | audit/readback/receipt/amendment exposed or narrowed existing truth |
| #235 | exposed | audit/readback/receipt/amendment exposed or narrowed existing truth |
| #236 | exposed | audit/readback/receipt/amendment exposed or narrowed existing truth |
| #237 | exposed | audit/readback/receipt/amendment exposed or narrowed existing truth |
| #238 | exposed | audit/readback/receipt/amendment exposed or narrowed existing truth |
| #239 | exposed | audit/readback/receipt/amendment exposed or narrowed existing truth |
| #240 | both | implementation introduced a seam and later amendment/readback exposed caveats |


## Rule

Do not blame the latest amendment for the original drift. The amendment often makes the truth visible. This map therefore separates introduction from exposure and marks `both` where an implementation-bearing PR creates a useful seam while also becoming part of a later amendment chain.

