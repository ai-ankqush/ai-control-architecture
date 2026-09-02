# Marketplace

The AI Control Architecture marketplace is a **neutral index of add-ons** that plug into the same core. It belongs to the ecosystem, not to any one vendor. Anyone can publish, every add-on is signed and integrity-checked, and each enterprise decides how much to trust. Neo Control lists its own products here on exactly the same rails as everyone else.

<p style="margin:18px 0 26px;">
<a href="https://marketplace.aicontrolarchitecture.org" target="_blank" rel="noopener" style="display:inline-block;padding:11px 22px;border-radius:8px;font-size:15px;font-weight:600;text-decoration:none;background:#2b6bff;color:#ffffff;margin-right:10px;">Browse the registry &rarr;</a>
<span style="font-size:13px;color:#8892a4;">The live, signed catalogue of add-ons lives at <b>marketplace.aicontrolarchitecture.org</b>. This page explains how it works.</span>
</p>

## What you can build

ACA is a small core plus six extension slots. An add-on is a directory with a manifest and an entry module, and it reads and writes only ACA objects (use case, control, evidence, assessment, finding, tier).

<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:14px;margin:20px 0;">
<div style="border:1px solid #232a39;border-radius:10px;padding:16px 18px;background:#0f1320;"><b style="color:#2b6bff;">collector</b><div style="font-size:13px;color:#8892a4;margin-top:5px;line-height:1.5;">Reads a system, emits ACA evidence. Connectors live here.</div></div>
<div style="border:1px solid #232a39;border-radius:10px;padding:16px 18px;background:#0f1320;"><b style="color:#2b6bff;">framework</b><div style="font-size:13px;color:#8892a4;margin-top:5px;line-height:1.5;">Crosswalks controls to an external standard or regulation.</div></div>
<div style="border:1px solid #232a39;border-radius:10px;padding:16px 18px;background:#0f1320;"><b style="color:#2b6bff;">control-pack</b><div style="font-size:13px;color:#8892a4;margin-top:5px;line-height:1.5;">Adds namespaced controls or a domain pack. Core ACA-* stays immutable.</div></div>
<div style="border:1px solid #232a39;border-radius:10px;padding:16px 18px;background:#0f1320;"><b style="color:#2b6bff;">test</b><div style="font-size:13px;color:#8892a4;margin-top:5px;line-height:1.5;">An assurance or adversarial check, emits test-result evidence.</div></div>
<div style="border:1px solid #232a39;border-radius:10px;padding:16px 18px;background:#0f1320;"><b style="color:#2b6bff;">renderer</b><div style="font-size:13px;color:#8892a4;margin-top:5px;line-height:1.5;">Turns an assessment into a report or export.</div></div>
<div style="border:1px solid #232a39;border-radius:10px;padding:16px 18px;background:#0f1320;"><b style="color:#2b6bff;">enforcer</b><div style="font-size:13px;color:#8892a4;margin-top:5px;line-height:1.5;">Acts at runtime on a decision. Paid enforcement plugs into this public interface.</div></div>
</div>

## Two tracks

| | Open track | Curated track |
|---|---|---|
| Who publishes | Anyone, permissionless | Reviewed submissions only |
| Certification | `ACA-Compatible` | `ACA-Verified` / `ACA-Certified` |
| Vetting | Automated | Automated, security, and behavioural (plus assurance for Certified) |
| Runtime | Always sandboxed, permission-prompted | Sandboxed; may be pre-trusted per enterprise policy |
| Paid add-ons | Not the place for them | Yes, this is where commercial add-ons live |
| Best for | The long tail, velocity, experimentation | Enterprise-safe adoption and monetisation |

An enterprise can set a policy of curated-only. An individual builder can live entirely in the open track.

## Every listing is verifiable

Transparency is the point. The decision an enterprise makes is "can I trust this," and each listing answers it up front:

- Certification badge (`Compatible` / `Verified` / `Certified`) and support tier
- Publisher identity (verified for paid and curated add-ons)
- Declared permissions (network, reads, writes, data scopes), shown **before** install
- Licence, version, and security-update status

Under the hood, every package carries a deterministic content hash and is **signed (Ed25519)**. Consumers verify the signature and re-check integrity on install, so a package changed since publish is rejected. A compromised or malicious add-on can be revoked centrally, and installed instances are disabled on the next check. The same registry serves a self-hosted core and a hosted one.

## The starter catalogue

The [reference add-ons](https://github.com/ai-ankqush/aca-plugins) are open and cover one per slot. Copy any of them as the starting point for your own.

<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:12px;margin:18px 0;">
<div style="border:1px solid #232a39;border-radius:10px;padding:14px 16px;background:#0f1320;font-size:13px;color:#c7d2e6;"><b>example-collector</b> <span style="color:#8892a4;">reads a system, emits evidence</span></div>
<div style="border:1px solid #232a39;border-radius:10px;padding:14px 16px;background:#0f1320;font-size:13px;color:#c7d2e6;"><b>example-framework</b> <span style="color:#8892a4;">crosswalk to NIST / ISO / OWASP / SR 11-7 / NYDFS</span></div>
<div style="border:1px solid #232a39;border-radius:10px;padding:14px 16px;background:#0f1320;font-size:13px;color:#c7d2e6;"><b>example-control-pack</b> <span style="color:#8892a4;">a namespaced control</span></div>
<div style="border:1px solid #232a39;border-radius:10px;padding:14px 16px;background:#0f1320;font-size:13px;color:#c7d2e6;"><b>example-test</b> <span style="color:#8892a4;">an assurance / adversarial check</span></div>
<div style="border:1px solid #232a39;border-radius:10px;padding:14px 16px;background:#0f1320;font-size:13px;color:#c7d2e6;"><b>example-renderer</b> <span style="color:#8892a4;">assessment to a Markdown report</span></div>
<div style="border:1px solid #232a39;border-radius:10px;padding:14px 16px;background:#0f1320;font-size:13px;color:#c7d2e6;"><b>example-enforcer</b> <span style="color:#8892a4;">shadow-mode reference for runtime</span></div>
</div>

## Publish your add-on

Scaffold from the reference core, then publish through the signed registry:

```bash
npx @aca/core new collector yourorg/your-connector

aca-registry keygen --out mykey
aca-registry publish ./your-connector --track open --key mykey.key.pem --publisher yourorg
```

<p style="margin:18px 0;">
<a href="https://github.com/ai-ankqush/aca-registry" target="_blank" rel="noopener" style="display:inline-block;padding:9px 18px;border-radius:8px;font-size:14px;font-weight:600;text-decoration:none;background:#2b6bff;color:#ffffff;margin-right:10px;">The registry (aca-registry)</a>
<a href="/explore/get-involved" style="display:inline-block;padding:9px 18px;border-radius:8px;font-size:14px;font-weight:600;text-decoration:none;border:1px solid #2b6bff;color:#8ab4ff;">List your add-on / become a Steward</a>
</p>

## Neutral by design

The marketplace is deployment-neutral: the same registry serves a self-hosted core and a hosted one, and no vendor owns the shelf. Neo Control is the founding steward and the first participant. Its own products, such as AI Supply Chain, Vendor Risk, Shadow AI, and the Action Fabric, list here as curated add-ons on the same rails as anyone else's, and compete on how well they work, not on owning the marketplace.

*This is v0.1 and evolving. The curated review board is Neo-stewarded today and moves to external assessors as ACA matures, with published, versioned criteria and an appeals path. See the [ecosystem RFC](/explore/ecosystem-rfc) for the full extension contracts and governance.*
