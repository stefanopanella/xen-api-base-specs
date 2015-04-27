Name:           xenvm
Version:        0.1.0
Release:        3%{?dist}
Summary:        A compatible replace for LVM supporting thinly provisioned volumes
License:        LGPL
URL:            https://github.com/xapi-project/xenvm
Source0:        https://github.com/xapi-project/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        refresh-demo
Source2:        resize-demo
Source3:        xenvm-nobisect.patch
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-cmdliner-devel
BuildRequires:  ocaml-rpc-devel
BuildRequires:  ocaml-sexplib-devel
BuildRequires:  ocaml-lwt-devel
BuildRequires:  ocaml-mirage-block-unix-devel
BuildRequires:  ocaml-cohttp-devel
BuildRequires:  ocaml-camldm-devel
BuildRequires:  ocaml-ounit-devel
BuildRequires:  ocaml-mirage-clock-unix-devel
BuildRequires:  ocaml-mirage-block-volume-devel
BuildRequires:  ocaml-uuidm-devel
BuildRequires:  ocaml-shared-block-ring-devel
BuildRequires:  ocaml-io-page-devel
BuildRequires:  ocaml-ctypes-devel
BuildRequires:  device-mapper-devel
BuildRequires:  libffi-devel
BuildRequires:  oasis

%description
A compatible replacement for LVM supporting thinly provisioned volumes.

%prep
%setup -q -n xenvm-%{version}
patch -p1 -N < %{SOURCE3} || (patch -R -p1 < %{SOURCE3} && patch -p1 < %{SOURCE3})

%build
make

%install
mkdir -p %{buildroot}/%{_sbindir}
install xenvmd.native %{buildroot}/%{_sbindir}/xenvmd
mkdir -p %{buildroot}/%{_bindir}
install xenvm.native %{buildroot}/%{_bindir}/xenvm
install local_allocator.native %{buildroot}/%{_bindir}/xenvm-local-allocator
mkdir -p %{buildroot}/opt/xensource/sm
cp %{SOURCE1} %{buildroot}/opt/xensource/sm
cp %{SOURCE2} %{buildroot}/opt/xensource/sm

%files
%doc README.md 
%{_sbindir}/xenvmd
%{_bindir}/xenvm
%{_bindir}/xenvm-local-allocator
/opt/xensource/sm/refresh-demo
/opt/xensource/sm/resize-demo

%changelog
* Thu Apr 23 2015 Jon Ludlam <jonathan.ludlam@citrix.com> - 0.1.0-3
- Add local allocator

* Wed Apr 22 2015 Jon Ludlam <jonathan.ludlam@citrix.com> - 0.1.0-2
- Add xenvm CLI

* Mon Apr 20 2015 Jon Ludlam <jonathan.ludlam@citrix.com> - 0.1.0-1
- Initial package

