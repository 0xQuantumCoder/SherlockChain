# SherlockChain: A Powerful Smart Contract Analysis Framework
<center>
<img src="https://i.ibb.co/y4187Bq/DALL-E-2024-05-02-21-17-35-Create-a-logo-for-Sherlock-Chain-ensuring-the-text-is-divided-into-two-li.webp" alt="SherlockChain Static Analysis Framework Logo" width="250" /></center>

SherlockChain is a powerful smart contract analysis framework that combines the capabilities of the renowned **Slither** tool with advanced AI-powered features. Developed by a team of security experts and AI researchers, SherlockChain offers unparalleled insights and vulnerability detection for Solidity, Vyper and Plutus smart contracts.

## Key Features

- **Comprehensive Vulnerability Detection**: SherlockChain's suite of detectors identifies a wide range of vulnerabilities, including high-impact issues like reentrancy, unprotected upgrades, and more.
- **AI-Powered Analysis**: Integrated AI models enhance the accuracy and precision of vulnerability detection, providing developers with actionable insights and recommendations.
- **Seamless Integration**: SherlockChain seamlessly integrates with popular development frameworks like Hardhat, Foundry, and Brownie, making it easy to incorporate into your existing workflow.
- **Intuitive Reporting**: SherlockChain generates detailed reports with clear explanations and code snippets, helping developers quickly understand and address identified issues.
- **Customizable Analyses**: The framework's flexible API allows users to write custom analyses and detectors, tailoring the tool to their specific needs.
- **Continuous Monitoring**: SherlockChain can be integrated into your CI/CD pipeline, providing ongoing monitoring and alerting for your smart contract codebase.

## Installation

To install SherlockChain, follow these steps:

```bash
git clone https://github.com/0xQuantumCoder/SherlockChain.git
cd SherlockChain
pip install .
```

## AI-Powered Features

SherlockChain's AI integration brings several advanced capabilities to the table:

1. **Intelligent Vulnerability Prioritization**: AI models analyze the context and potential impact of detected vulnerabilities, providing developers with a prioritized list of issues to address.
2. **Automated Remediation Suggestions**: The AI component suggests potential fixes and code modifications to address identified vulnerabilities, accelerating the remediation process.
3. **Proactive Security Auditing**: SherlockChain's AI models continuously monitor your codebase, proactively identifying emerging threats and providing early warning signals.
4. **Natural Language Interaction**: Users can interact with SherlockChain using natural language, allowing them to query the tool, request specific analyses, and receive detailed responses.
he `--help` command in the SherlockChain framework provides a comprehensive overview of all the available options and features. It includes information on:

- **Vulnerability Detection**: The `--detect` and `--exclude-detectors` options allow users to specify which vulnerability detectors to run, including both built-in and AI-powered detectors.
- **Reporting**: The `--report-format`, `--report-output`, and various `--report-*` options control how the analysis results are reported, including the ability to generate reports in different formats (JSON, Markdown, SARIF, etc.).
- **Filtering**: The `--filter-*` options enable users to filter the reported issues based on severity, impact, confidence, and other criteria.
- **AI Integration**: The `--ai-*` options allow users to configure and control the AI-powered features of SherlockChain, such as prioritizing high-impact vulnerabilities, enabling specific AI detectors, and managing AI model configurations.
- **Integration with Development Frameworks**: Options like `--truffle` and `--truffle-build-directory` facilitate the integration of SherlockChain into popular development frameworks like Truffle.
- **Miscellaneous Options**: Additional options for compiling contracts, listing detectors, and customizing the analysis process.

The `--help` command provides a detailed explanation of each option, its purpose, and how to use it, making it a valuable resource for users to quickly understand and leverage the full capabilities of the SherlockChain framework.

Example usage:

```bash
sherlockchain --help
```

This will display the comprehensive usage guide for the SherlockChain framework, including all available options and their descriptions.
```bash
usage: sherlockchain [-h] [--version] [--solc-remaps SOLC_REMAPS] [--solc-settings SOLC_SETTINGS]
                    [--solc-version SOLC_VERSION] [--truffle] [--truffle-build-directory TRUFFLE_BUILD_DIRECTORY]
                    [--truffle-config-file TRUFFLE_CONFIG_FILE] [--compile] [--list-detectors]
                    [--list-detectors-info] [--detect DETECTORS] [--exclude-detectors EXCLUDE_DETECTORS]
                    [--print-issues] [--json] [--markdown] [--sarif] [--text] [--zip] [--output OUTPUT]
                    [--filter-paths FILTER_PATHS] [--filter-paths-exclude FILTER_PATHS_EXCLUDE]
                    [--filter-contracts FILTER_CONTRACTS] [--filter-contracts-exclude FILTER_CONTRACTS_EXCLUDE]
                    [--filter-severity FILTER_SEVERITY] [--filter-impact FILTER_IMPACT]
                    [--filter-confidence FILTER_CONFIDENCE] [--filter-check-suicidal]
                    [--filter-check-upgradeable] [--filter-check-erc20] [--filter-check-erc721]
                    [--filter-check-reentrancy] [--filter-check-gas-optimization] [--filter-check-code-quality]
                    [--filter-check-best-practices] [--filter-check-ai-detectors] [--filter-check-all]
                    [--filter-check-none] [--check-all] [--check-suicidal] [--check-upgradeable]
                    [--check-erc20] [--check-erc721] [--check-reentrancy] [--check-gas-optimization]
                    [--check-code-quality] [--check-best-practices] [--check-ai-detectors] [--check-none]
                    [--check-all-detectors] [--check-all-severity] [--check-all-impact] [--check-all-confidence]
                    [--check-all-categories] [--check-all-filters] [--check-all-options] [--check-all]
                    [--check-none] [--report-format {json,markdown,sarif,text,zip}] [--report-output OUTPUT]
                    [--report-severity REPORT_SEVERITY] [--report-impact REPORT_IMPACT]
                    [--report-confidence REPORT_CONFIDENCE] [--report-check-suicidal]
                    [--report-check-upgradeable] [--report-check-erc20] [--report-check-erc721]
                    [--report-check-reentrancy] [--report-check-gas-optimization] [--report-check-code-quality]
                    [--report-check-best-practices] [--report-check-ai-detectors] [--report-check-all]
                    [--report-check-none] [--report-all] [--report-suicidal] [--report-upgradeable]
                    [--report-erc20] [--report-erc721] [--report-reentrancy] [--report-gas-optimization]
                    [--report-code-quality] [--report-best-practices] [--report-ai-detectors] [--report-none]
                    [--report-all-detectors] [--report-all-severity] [--report-all-impact]
                    [--report-all-confidence] [--report-all-categories] [--report-all-filters]
                    [--report-all-options] [--report-all] [--report-none] [--ai-enabled] [--ai-disabled]
                    [--ai-priority-high] [--ai-priority-medium] [--ai-priority-low] [--ai-priority-all]
                    [--ai-priority-none] [--ai-confidence-high] [--ai-confidence-medium] [--ai-confidence-low]
                    [--ai-confidence-all] [--ai-confidence-none] [--ai-detectors-all] [--ai-detectors-none]
                    [--ai-detectors-specific AI_DETECTORS_SPECIFIC] [--ai-detectors-exclude AI_DETECTORS_EXCLUDE]
                    [--ai-models-path AI_MODELS_PATH] [--ai-models-update] [--ai-models-download]
                    [--ai-models-list] [--ai-models-info] [--ai-models-version] [--ai-models-check]
                    [--ai-models-upgrade] [--ai-models-remove] [--ai-models-clean] [--ai-models-reset]
                    [--ai-models-backup] [--ai-models-restore] [--ai-models-export] [--ai-models-import]
                    [--ai-models-config AI_MODELS_CONFIG] [--ai-models-config-update] [--ai-models-config-reset]
                    [--ai-models-config-export] [--ai-models-config-import] [--ai-models-config-list]
                    [--ai-models-config-info] [--ai-models-config-version] [--ai-models-config-check]
                    [--ai-models-config-upgrade] [--ai-models-config-remove] [--ai-models-config-clean]
                    [--ai-models-config-reset] [--ai-models-config-backup] [--ai-models-config-restore]
                    [--ai-models-config-export] [--ai-models-config-import] [--ai-models-config-path AI_MODELS_CONFIG_PATH]
                    [--ai-models-config-file AI_MODELS_CONFIG_FILE] [--ai-models-config-url AI_MODELS_CONFIG_URL]
                    [--ai-models-config-name AI_MODELS_CONFIG_NAME] [--ai-models-config-description AI_MODELS_CONFIG_DESCRIPTION]
                    [--ai-models-config-version-major AI_MODELS_CONFIG_VERSION_MAJOR]
                    [--ai-models-config-version-minor AI_MODELS_CONFIG_VERSION_MINOR]
                    [--ai-models-config-version-patch AI_MODELS_CONFIG_VERSION_PATCH]
                    [--ai-models-config-author AI_MODELS_CONFIG_AUTHOR]
                    [--ai-models-config-license AI_MODELS_CONFIG_LICENSE]
                    [--ai-models-config-url-documentation AI_MODELS_CONFIG_URL_DOCUMENTATION]
                    [--ai-models-config-url-source AI_MODELS_CONFIG_URL_SOURCE]
                    [--ai-models-config-url-issues AI_MODELS_CONFIG_URL_ISSUES]
                    [--ai-models-config-url-changelog AI_MODELS_CONFIG_URL_CHANGELOG]
                    [--ai-models-config-url-support AI_MODELS_CONFIG_URL_SUPPORT]
                    [--ai-models-config-url-website AI_MODELS_CONFIG_URL_WEBSITE]
                    [--ai-models-config-url-logo AI_MODELS_CONFIG_URL_LOGO]
                    [--ai-models-config-url-icon AI_MODELS_CONFIG_URL_ICON]
                    [--ai-models-config-url-banner AI_MODELS_CONFIG_URL_BANNER]
                    [--ai-models-config-url-screenshot AI_MODELS_CONFIG_URL_SCREENSHOT]
                    [--ai-models-config-url-video AI_MODELS_CONFIG_URL_VIDEO]
                    [--ai-models-config-url-demo AI_MODELS_CONFIG_URL_DEMO]
                    [--ai-models-config-url-documentation-api AI_MODELS_CONFIG_URL_DOCUMENTATION_API]
                    [--ai-models-config-url-documentation-user AI_MODELS_CONFIG_URL_DOCUMENTATION_USER]
                    [--ai-models-config-url-documentation-developer AI_MODELS_CONFIG_URL_DOCUMENTATION_DEVELOPER]
                    [--ai-models-config-url-documentation-faq AI_MODELS_CONFIG_URL_DOCUMENTATION_FAQ]
                    [--ai-models-config-url-documentation-tutorial AI_MODELS_CONFIG_URL_DOCUMENTATION_TUTORIAL]
                    [--ai-models-config-url-documentation-guide AI_MODELS_CONFIG_URL_DOCUMENTATION_GUIDE]
                    [--ai-models-config-url-documentation-whitepaper AI_MODELS_CONFIG_URL_DOCUMENTATION_WHITEPAPER]
                    [--ai-models-config-url-documentation-roadmap AI_MODELS_CONFIG_URL_DOCUMENTATION_ROADMAP]
                    [--ai-models-config-url-documentation-blog AI_MODELS_CONFIG_URL_DOCUMENTATION_BLOG]
                    [--ai-models-config-url-documentation-community AI_MODELS_CONFIG_URL_DOCUMENTATION_COMMUNITY]
```
This comprehensive usage guide provides information on all the available options and features of the SherlockChain framework, including:

- Vulnerability detection options: `--detect`, `--exclude-detectors`
- Reporting options: `--report-format`, `--report-output`, `--report-*`
- Filtering options: `--filter-*`
- AI integration options: `--ai-*`
- Integration with development frameworks: `--truffle`, `--truffle-build-directory`
- Miscellaneous options: `--compile`, `--list-detectors`, `--list-detectors-info`

By reviewing this comprehensive usage guide, you can quickly understand how to leverage the full capabilities of the SherlockChain framework to analyze your smart contracts and identify potential vulnerabilities. This will help you ensure the security and reliability of your DeFi protocol before deployment.

## AI-Powered Detectors

Num | Detector | What it Detects | Impact | Confidence
--- | --- | --- | --- | ---
1 | `ai-anomaly-detection` | [Detect anomalous code patterns using advanced AI models](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#ai-anomaly-detection) | High | High
2 | `ai-vulnerability-prediction` | [Predict potential vulnerabilities using machine learning](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#ai-vulnerability-prediction) | High | High
3 | `ai-code-optimization` | [Suggest code optimizations based on AI-driven analysis](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#ai-code-optimization) | Medium | High
4 | `ai-contract-complexity` | [Assess contract complexity and maintainability using AI](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#ai-contract-complexity) | Medium | High
5 | `ai-gas-optimization` | [Identify gas-optimizing opportunities with AI](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#ai-gas-optimization) | Medium | Medium
## Detectors

Num | Detector | What it Detects | Impact | Confidence
--- | --- | --- | --- | ---
1 | `abiencoderv2-array` | [Storage abiencoderv2 array](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#storage-abiencoderv2-array) | High | High
2 | `arbitrary-send-erc20` | [transferFrom uses arbitrary `from`](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#arbitrary-from-in-transferfrom) | High | High
3 | `array-by-reference` | [Modifying storage array by value](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#modifying-storage-array-by-value) | High | High
4 | `encode-packed-collision` | [ABI encodePacked Collision](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#abi-encodePacked-collision) | High | High
5 | `incorrect-shift` | [The order of parameters in a shift instruction is incorrect.](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#incorrect-shift-in-assembly) | High | High
6 | `multiple-constructors` | [Multiple constructor schemes](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#multiple-constructor-schemes) | High | High
7 | `name-reused` | [Contract's name reused](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#name-reused) | High | High
8 | `protected-vars` | [Detected unprotected variables](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#protected-variables) | High | High
9 | `public-mappings-nested` | [Public mappings with nested variables](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#public-mappings-with-nested-variables) | High | High
10 | `rtlo` | [Right-To-Left-Override control character is used](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#right-to-left-override-character) | High | High
11 | `shadowing-state` | [State variables shadowing](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#state-variable-shadowing) | High | High
12 | `suicidal` | [Functions allowing anyone to destruct the contract](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#suicidal) | High | High
13 | `uninitialized-state` | [Uninitialized state variables](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#uninitialized-state-variables) | High | High
14 | `uninitialized-storage` | [Uninitialized storage variables](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#uninitialized-storage-variables) | High | High
15 | `unprotected-upgrade` | [Unprotected upgradeable contract](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#unprotected-upgradeable-contract) | High | High
16 | `codex` | [Use Codex to find vulnerabilities.](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#codex) | High | Low
17 | `arbitrary-send-erc20-permit` | [transferFrom uses arbitrary from with permit](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#arbitrary-from-in-transferfrom-used-with-permit) | High | Medium
18 | `arbitrary-send-eth` | [Functions that send Ether to arbitrary destinations](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#functions-that-send-ether-to-arbitrary-destinations) | High | Medium
19 | `controlled-array-length` | [Tainted array length assignment](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#array-length-assignment) | High | Medium
20 | `controlled-delegatecall` | [Controlled delegatecall destination](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#controlled-delegatecall) | High | Medium
21 | `delegatecall-loop` | [Payable functions using `delegatecall` inside a loop](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation/#payable-functions-using-delegatecall-inside-a-loop) | High | Medium
22 | `incorrect-exp` | [Incorrect exponentiation](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#incorrect-exponentiation) | High | Medium
23 | `incorrect-return` | [If a `return` is incorrectly used in assembly mode.](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#incorrect-return-in-assembly) | High | Medium
24 | `msg-value-loop` | [msg.value inside a loop](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation/#msgvalue-inside-a-loop) | High | Medium
25 | `reentrancy-eth` | [Reentrancy vulnerabilities (theft of ethers)](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#reentrancy-vulnerabilities) | High | Medium
26 | `return-leave` | [If a `return` is used instead of a `leave`.](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#return-instead-of-leave-in-assembly) | High | Medium
27 | `storage-array` | [Signed storage integer array compiler bug](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#storage-signed-integer-array) | High | Medium
28 | `unchecked-transfer` | [Unchecked tokens transfer](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#unchecked-transfer) | High | Medium
29 | `weak-prng` | [Weak PRNG](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#weak-PRNG) | High | Medium
30 | `domain-separator-collision` | [Detects ERC20 tokens that have a function whose signature collides with EIP-2612's DOMAIN_SEPARATOR()](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#domain-separator-collision) | Medium | High
31 | `enum-conversion` | [Detect dangerous enum conversion](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#dangerous-enum-conversion) | Medium | High
32 | `erc20-interface` | [Incorrect ERC20 interfaces](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#incorrect-erc20-interface) | Medium | High
33 | `erc721-interface` | [Incorrect ERC721 interfaces](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#incorrect-erc721-interface) | Medium | High
34 | `incorrect-equality` | [Dangerous strict equalities](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#dangerous-strict-equalities) | Medium | High
35 | `locked-ether` | [Contracts that lock ether](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#contracts-that-lock-ether) | Medium | High
36 | `mapping-deletion` | [Deletion on mapping containing a structure](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#deletion-on-mapping-containing-a-structure) | Medium | High
37 | `shadowing-abstract` | [State variables shadowing from abstract contracts](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#state-variable-shadowing-from-abstract-contracts) | Medium | High
38 | `tautological-compare` | [Comparing a variable to itself always returns true or false, depending on comparison](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#tautological-compare) | Medium | High
39 | `tautology` | [Tautology or contradiction](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#tautology-or-contradiction) | Medium | High
40 | `write-after-write` | [Unused write](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#write-after-write) | Medium | High
41 | `boolean-cst` | [Misuse of Boolean constant](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#misuse-of-a-boolean-constant) | Medium | Medium
42 | `constant-function-asm` | [Constant functions using assembly code](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#constant-functions-using-assembly-code) | Medium | Medium
43 | `constant-function-state` | [Constant functions changing the state](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#constant-functions-changing-the-state) | Medium | Medium
44 | `divide-before-multiply` | [Imprecise arithmetic operations order](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#divide-before-multiply) | Medium | Medium
45 | `out-of-order-retryable` | [Out-of-order retryable transactions](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#out-of-order-retryable-transactions) | Medium | Medium
46 | `reentrancy-no-eth` | [Reentrancy vulnerabilities (no theft of ethers)](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#reentrancy-vulnerabilities-1) | Medium | Medium
47 | `reused-constructor` | [Reused base constructor](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#reused-base-constructors) | Medium | Medium
48 | `tx-origin` | [Dangerous usage of `tx.origin`](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#dangerous-usage-of-txorigin) | Medium | Medium
49 | `unchecked-lowlevel` | [Unchecked low-level calls](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#unchecked-low-level-calls) | Medium | Medium
50 | `unchecked-send` | [Unchecked send](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#unchecked-send) | Medium | Medium
51 | `uninitialized-local` | [Uninitialized local variables](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#uninitialized-local-variables) | Medium | Medium
52 | `unused-return` | [Unused return values](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#unused-return) | Medium | Medium
53 | `incorrect-modifier` | [Modifiers that can return the default value](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#incorrect-modifier) | Low | High
54 | `shadowing-builtin` | [Built-in symbol shadowing](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#builtin-symbol-shadowing) | Low | High
55 | `shadowing-local` | [Local variables shadowing](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#local-variable-shadowing) | Low | High
56 | `uninitialized-fptr-cst` | [Uninitialized function pointer calls in constructors](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#uninitialized-function-pointers-in-constructors) | Low | High
57 | `variable-scope` | [Local variables used prior their declaration](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#pre-declaration-usage-of-local-variables) | Low | High
58 | `void-cst` | [Constructor called not implemented](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#void-constructor) | Low | High
59 | `calls-loop` | [Multiple calls in a loop](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation/#calls-inside-a-loop) | Low | Medium
60 | `events-access` | [Missing Events Access Control](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#missing-events-access-control) | Low | Medium
61 | `events-maths` | [Missing Events Arithmetic](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#missing-events-arithmetic) | Low | Medium
62 | `incorrect-unary` | [Dangerous unary expressions](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#dangerous-unary-expressions) | Low | Medium
63 | `missing-zero-check` | [Missing Zero Address Validation](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#missing-zero-address-validation) | Low | Medium
64 | `reentrancy-benign` | [Benign reentrancy vulnerabilities](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#reentrancy-vulnerabilities-2) | Low | Medium
65 | `reentrancy-events` | [Reentrancy vulnerabilities leading to out-of-order Events](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#reentrancy-vulnerabilities-3) | Low | Medium
66 | `return-bomb` | [A low level callee may consume all callers gas unexpectedly.](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#return-bomb) | Low | Medium
67 | `timestamp` | [Dangerous usage of `block.timestamp`](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#block-timestamp) | Low | Medium
68 | `assembly` | [Assembly usage](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#assembly-usage) | Informational | High
69 | `assert-state-change` | [Assert state change](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#assert-state-change) | Informational | High
70 | `boolean-equal` | [Comparison to boolean constant](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#boolean-equality) | Informational | High
71 | `cyclomatic-complexity` | [Detects functions with high (> 11) cyclomatic complexity](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#cyclomatic-complexity) | Informational | High
72 | `deprecated-standards` | [Deprecated Solidity Standards](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#deprecated-standards) | Informational | High
73 | `erc20-indexed` | [Un-indexed ERC20 event parameters](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#unindexed-erc20-event-parameters) | Informational | High
74 | `function-init-state` | [Function initializing state variables](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#function-initializing-state) | Informational | High
75 | `incorrect-using-for` | [Detects using-for statement usage when no function from a given library matches a given type](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#incorrect-using-for-usage) | Informational | High
76 | `low-level-calls` | [Low level calls](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#low-level-calls) | Informational | High
77 | `missing-inheritance` | [Missing inheritance](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#missing-inheritance) | Informational | High
78 | `naming-convention` | [Conformity to Solidity naming conventions](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#conformance-to-solidity-naming-conventions) | Informational | High
79 | `pragma` | [If different pragma directives are used](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#different-pragma-directives-are-used) | Informational | High
80 | `redundant-statements` | [Redundant statements](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#redundant-statements) | Informational | High
81 | `solc-version` | [Incorrect Solidity version](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#incorrect-versions-of-solidity) | Informational | High
82 | `unimplemented-functions` | [Unimplemented functions](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#unimplemented-functions) | Informational | High
83 | `unused-import` | [Detects unused imports](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#unused-imports) | Informational | High
84 | `unused-state` | [Unused state variables](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#unused-state-variable) | Informational | High
85 | `costly-loop` | [Costly operations in a loop](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#costly-operations-inside-a-loop) | Informational | Medium
86 | `dead-code` | [Functions that are not used](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#dead-code) | Informational | Medium
87 | `reentrancy-unlimited-gas` | [Reentrancy vulnerabilities through send and transfer](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#reentrancy-vulnerabilities-4) | Informational | Medium
88 | `similar-names` | [Variable names are too similar](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#variable-names-too-similar) | Informational | Medium
89 | `too-many-digits` | [Conformance to numeric notation best practices](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#too-many-digits) | Informational | Medium
90 | `cache-array-length` | [Detects `for` loops that use `length` member of some storage array in their loop condition and don't modify it.](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#cache-array-length) | Optimization | High
91 | `constable-states` | [State variables that could be declared constant](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#state-variables-that-could-be-declared-constant) | Optimization | High
92 | `external-function` | [Public function that could be declared external](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#public-function-that-could-be-declared-external) | Optimization | High
93 | `immutable-states` | [State variables that could be declared immutable](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#state-variables-that-could-be-declared-immutable) | Optimization | High
94 | `var-read-using-this` | [Contract reads its own variable using `this`](https://github.com/0xQuantumCoder/SherlockChain/wiki/Detector-Documentation#public-variable-read-in-external-context) | Optimization | High
