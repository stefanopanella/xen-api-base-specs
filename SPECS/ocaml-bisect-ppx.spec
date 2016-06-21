%global debug_package %{nil}

Name:           ocaml-bisect-ppx
Version:        1.1.0
Release:        1%{?dist}
Summary:        A tool for code coverage profiling
License:        GPLv3
URL:            https://github.com/aantron/bisect_ppx
Source0:        https://github.com/aantron/bisect_ppx/archive/%{version}/%{name}-%{version}.tar.gz     
BuildRequires:  ocaml
BuildRequires:  ocaml-ppxtools-devel
BuildRequires:  ocaml-findlib

%description
A coverage profiler for OCaml projects.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n bisect_ppx-%{version}

%build
make build

%install
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
make install

%files
%doc README.md
%doc doc/*
%{_libdir}/ocaml/bisect_ppx
%exclude %{_libdir}/ocaml/bisect_ppx/*.a
%exclude %{_libdir}/ocaml/bisect_ppx/*.cmxa
%exclude %{_libdir}/ocaml/bisect_ppx/*.cmx
# %exclude %{_libdir}/ocaml/bisect_ppx/*.mli

%files devel
%{_libdir}/ocaml/bisect_ppx/*.a
%{_libdir}/ocaml/bisect_ppx/*.cmx
%{_libdir}/ocaml/bisect_ppx/*.cmxa
# %{_libdir}/ocaml/bisect_ppx/*.mli

%changelog
* Wed May 11 2016 Christian Lindig <christian.lindig@citrix.com> - 1.1.0-1
- Initial package
