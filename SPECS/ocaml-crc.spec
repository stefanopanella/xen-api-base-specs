%define debug_package %{nil}

Name:           ocaml-crc
Version:        1.0.0
Release:        1%{?dist}
Summary:        CRC implementation for OCaml
License:        ISC
URL:            https://github.com/xapi-project/ocaml-crc/
Source0:        https://github.com/xapi-project/ocaml-crc/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  oasis
BuildRequires:  ocaml
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-cstruct-devel
BuildRequires:  ocaml-ounit-devel
Requires:       ocaml
Requires:       ocaml-findlib

%description
CRC implementation for OCaml, allowing you to compute checksums of cstructs
and strings.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q

%build
ocaml setup.ml -configure --destdir %{buildroot}%{_libdir}/ocaml
ocaml setup.ml -build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml
export OCAMLFIND_LDCONF=%{buildroot}%{_libdir}/ocaml/ld.conf
ocaml setup.ml -install

%files
%{_libdir}/ocaml/crc
%{_libdir}/ocaml/crc/META
%{_libdir}/ocaml/crc/crc.cma
%{_libdir}/ocaml/crc/crc.cmi
%{_libdir}/ocaml/crc/dllcrc_stubs.so

%files devel
%doc ChangeLog README.md
%{_libdir}/ocaml/crc/crc.a
%{_libdir}/ocaml/crc/crc.annot
%{_libdir}/ocaml/crc/crc.cmt
%{_libdir}/ocaml/crc/crc.cmti
%{_libdir}/ocaml/crc/crc.cmx
%{_libdir}/ocaml/crc/crc.cmxa
%{_libdir}/ocaml/crc/crc.cmxs
%{_libdir}/ocaml/crc/crc.mli
%{_libdir}/ocaml/crc/libcrc_stubs.a
%{_libdir}/ocaml/crc/crc.cmt
%{_libdir}/ocaml/crc/crc.cmti
%{_libdir}/ocaml/crc/crc.annot

%changelog
* Thu Apr 28 2016 Euan Harris <euan.harris@citrix.com> - 1.0.0-1
- Update to 1.0.0

* Fri Apr 22 2016 Si Beaumont <simon.beaumont@citrix.com> - 0.9.9-1
- Update to 0.9.9

* Sat Apr 26 2014 David Scott <dave.scott@citrix.com> - 0.9.1-1
- Update to 0.9.1

* Thu Dec 12 2013 John Else <john.else@citrix.com> - 0.9.0-1
- Initial package
