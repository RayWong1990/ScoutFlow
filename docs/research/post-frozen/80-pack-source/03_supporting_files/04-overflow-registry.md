# Overflow Registry

| Item | Blocked reason | Reopen condition | Human gate |
|---|---|---|---|
| true vault write | preview-only loop and RAW handoff proof not yet sufficient for write approval | C2 pass + explicit true_write_approval | true_write_approval |
| BBDown live / yt-dlp | runtime not approved; credential/platform risks | separate runtime dispatch + explicit_runtime_approval | explicit_runtime_approval |
| ffmpeg / ASR / audio_transcript | current phase blocks audio runtime | phase gate + proof + explicit approval | explicit_runtime_approval |
| browser automation / Playwright execution | no human visual verdict yet | screenshot packet + human visual verdict + explicit browser approval | visual_verdict |
| DBvNext / migrations | migrations forbidden; DBvNext candidate only | migration design + external audit + explicit migration approval | explicit_migration_approval |
| full Signal Workbench | over-objectification risk | C1/C2 pass and object compression closeout | usefulness_verdict |
