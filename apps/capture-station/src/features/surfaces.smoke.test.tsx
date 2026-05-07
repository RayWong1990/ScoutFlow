import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";

import AppShellOverview from "../components/AppShell/AppShellOverview";
import CapturePlan from "./capture-plan/CapturePlan";
import CaptureScope from "./capture-scope/CaptureScope";
import DensitySpec from "./_specs/DensitySpec";
import LiveMetadata from "./live-metadata/LiveMetadata";
import SignalHypothesis from "./signal-hypothesis/SignalHypothesis";
import TopicCardLite from "./topic-card-preview/TopicCardLite";
import TopicCardVault from "./topic-card-vault/TopicCardVault";
import TrustTrace from "./trust-trace/TrustTrace";
import UrlBar from "./url-bar/UrlBar";
import VaultCommit from "./vault-commit/VaultCommit";
import VaultPreview from "./vault-preview/VaultPreview";
import TypeSpec from "./_specs/TypeSpec";

describe("surface smoke tests", () => {
  it("renders app shell overview", () => {
    render(<AppShellOverview />);
    expect(screen.getByText("应用总览")).toBeTruthy();
  });

  it("renders url bar surface", () => {
    render(<UrlBar />);
    expect(screen.getByText("URL 输入栏状态集")).toBeTruthy();
  });

  it("renders live metadata surface", () => {
    render(<LiveMetadata />);
    expect(screen.getByText("实时元数据状态集")).toBeTruthy();
  });

  it("renders capture scope surface", () => {
    render(<CaptureScope />);
    expect(screen.getByText("采集范围状态集")).toBeTruthy();
  });

  it("renders trust trace surface", () => {
    render(<TrustTrace />);
    expect(screen.getByText("信任溯源状态集")).toBeTruthy();
  });

  it("renders vault preview surface", () => {
    render(<VaultPreview />);
    expect(screen.getByText("入库预览状态集")).toBeTruthy();
  });

  it("renders vault commit surface", () => {
    render(<VaultCommit />);
    expect(screen.getByText("入库提交状态集")).toBeTruthy();
  });

  it("renders topic card lite surface", () => {
    render(<TopicCardLite />);
    expect(screen.getByText("Topic Card Lite 状态集")).toBeTruthy();
  });

  it("renders topic card vault surface", () => {
    render(<TopicCardVault />);
    expect(screen.getByText("Topic Card Vault 状态集")).toBeTruthy();
  });

  it("renders signal hypothesis surface", () => {
    render(<SignalHypothesis />);
    expect(screen.getByText("信号 / 假设信息架构状态集")).toBeTruthy();
  });

  it("renders capture plan surface", () => {
    render(<CapturePlan />);
    expect(screen.getByText("采集计划信息架构状态集")).toBeTruthy();
  });

  it("renders density spec surface", () => {
    render(<DensitySpec />);
    expect(screen.getByText("密度规格 · V3 紧凑密度")).toBeTruthy();
  });

  it("renders type spec surface", () => {
    render(<TypeSpec />);
    expect(screen.getByText("字重规格 · V4 高字重")).toBeTruthy();
  });
});
