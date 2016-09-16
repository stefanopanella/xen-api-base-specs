%global opt %(test -x %{_bindir}/ocamlopt && echo 1 || echo 0)

Name:           ocaml-systemd
Version:        1.1
Release:        1%{?dist}
Summary:        Ocaml Systemd bindings

License:        LGPL-3 with OCaml linking exception
URL:            https://github.com/juergenhoetzel/ocaml-systemd
Source0:        https://github.com/juergenhoetzel/ocaml-systemd/archive/%{version}/ocaml-systemd-%{version}.tar.gz

BuildRequires:  ocaml >= 4.02.0
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-ocamldoc
BuildRequires:  chrpath
BuildRequires:  systemd-devel
BuildRequires:  oasis

%description
Ocaml systemd library bindings

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       systemd-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup

%build
oasis setup
make

%install
# These rules work if the library uses 'ocamlfind install' to install itself.
export DESTDIR=$RPM_BUILD_ROOT
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
make install

%files
%doc README.txt README.md
%dir %{_libdir}/ocaml/systemd/
%{_libdir}/ocaml/systemd/META
%{_libdir}/ocaml/systemd/*.cma
%{_libdir}/ocaml/systemd/*.cmi
%if %opt
%exclude %{_libdir}/ocaml/systemd/*.a
%exclude %{_libdir}/ocaml/systemd/*.cmxa
%exclude %{_libdir}/ocaml/systemd/*.cmx
%exclude %{_libdir}/ocaml/systemd/*.cmt
%exclude %{_libdir}/ocaml/systemd/*.cmti
%exclude %{_libdir}/ocaml/systemd/*.cmxs
%endif
%exclude %{_libdir}/ocaml/*/*.mli
%{_libdir}/ocaml/stublibs/*.so
%{_libdir}/ocaml/stublibs/*.so.owner

%files devel
%doc README.txt README.md
%if %opt
%{_libdir}/ocaml/systemd/*.annot
%{_libdir}/ocaml/systemd/*.a
%{_libdir}/ocaml/systemd/*.cmxa
%{_libdir}/ocaml/systemd/*.cmx
%{_libdir}/ocaml/systemd/*.cmt
%{_libdir}/ocaml/systemd/*.cmti
%{_libdir}/ocaml/systemd/*.cmxs
%endif
%{_libdir}/ocaml/*/*.mli

%changelog
 * Wed Jun 29 2016 Rafal Mielniczuk <rafal.mielniczuk@eu.citrix.com> - 1.1-1
 - Initial package
