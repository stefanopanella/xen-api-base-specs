%global debug_package %{nil}

Name:           ocaml-ppxtools
Version:        5.0+4.02.0
Release:        1%{?dist}
Summary:        A tool for code coverage profiling
License:        MIT
URL:            https://github.com/alainfrisch/ppx_tools
Source0:        https://github.com/alainfrisch/ppx_tools/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib

%description
Tools for authors of syntactic tools (such as ppx rewriters).

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n ppx_tools-5.0-4.02.0

%build
make

%install
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
make install


%files
%doc LICENSE
%doc README.md
%{_libdir}/ocaml/ppx_tools
%exclude %{_libdir}/ocaml/ppx_tools/*.a
%exclude %{_libdir}/ocaml/ppx_tools/*.cmxa
%exclude %{_libdir}/ocaml/ppx_tools/*.cmx
%exclude %{_libdir}/ocaml/ppx_tools/*.mli

%files devel
%{_libdir}/ocaml/ppx_tools/*.a
%{_libdir}/ocaml/ppx_tools/*.cmx
%{_libdir}/ocaml/ppx_tools/*.cmxa
%{_libdir}/ocaml/ppx_tools/*.mli

%changelog
* Wed May 11 2016 Christian Lindig <christian.lindig@citrix.com> - 5.0+4.02.0-1
- Initial package

