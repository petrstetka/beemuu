# macOS ARM64 community build

This fork builds BeeEmUu for Apple Silicon (including M5) on GitHub's
`macos-15` ARM64 runner. Nothing needs to be compiled on the destination Mac.
The target is `aarch64-apple-darwin`, with macOS 12.0 as the deployment minimum.
This is a community build, not an official upstream macOS release.

## Download and install

Open the fork's **Actions → macOS ARM64 community build**, select a successful
run, and download the `BeeEmUu-macos-arm64-<run number>` artifact. GitHub may
require you to sign in. Artifacts expire after 30 days; save the download.

The artifact contains a DMG, a ZIP preserving the app bundle, matching source,
the GPL license, build information, and SHA-256 checksums. Open the DMG and
drag BeeEmUu into Applications. The app is ad-hoc signed, with no Apple
Developer ID or notarization. macOS may require explicit approval under
System Settings → Privacy & Security before first launch.

Start with the built-in Simulator. Build success and unit tests do not verify
the macOS webview, a real K+DCAN adapter, FTDI timing, or a particular vehicle.
Serial ports on macOS usually have names such as `/dev/cu.usbserial-*`.

## Rebuild

Push source changes to `macos-arm64` to run tests and build automatically.
To use **Run workflow**, GitHub requires the workflow to exist on the default
branch. Until it is merged there, use the branch's push trigger instead.
No upstream changes are merged automatically: review and merge them into
`macos-arm64` first. No release tag, publishing credential, or updater key is
required. The workflow has read-only repository permissions and uploads a
run artifact rather than creating an upstream release.

The macOS configuration bundles community data under `Contents/Resources`.
The directory lookup also supports that standard macOS bundle location.
The build replaces only the generated automatic-update script with a no-op;
it does not change the updater source used by other platforms. Automatic
updates are disabled for this build because upstream signing credentials and
published macOS updater packages are unavailable. Download later builds
manually. The original configuration for Windows and Linux is unchanged.

All compilation and the JavaScript, Python, and Rust tests run on GitHub.
The packaging step verifies ARM64 architecture, the app signature, bundled
community data, and DMG integrity. The matching source archive plus the
configuration and workflow record how to rebuild the package.
