Name:           ocaml-inotify
Version:        2.3
Release:        1%{?dist}
Summary:        Inotify bindings for OCaml.

Group:          Development/Libraries
License:        LGPLv2 with exceptions
URL:            https://github.com/whitequark/ocaml-inotify
Source0:        https://github.com/whitequark/ocaml-inotify/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  ocaml >= 4.02.2
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-ounit-devel
BuildRequires:  ocaml-fileutils-devel
BuildRequires:  m4
BuildRequires:  chrpath
BuildRequires:  oasis

%description
Inotify bindings for OCaml.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup

%build
ocaml setup.ml -configure --prefix %{_prefix} \
      --libdir %{_libdir} \
      --libexecdir %{_libexecdir} \
      --exec-prefix %{_exec_prefix} \
      --bindir %{_bindir} \
      --sbindir %{_sbindir} \
      --mandir %{_mandir} \
      --datadir %{_datadir} \
      --localstatedir %{_localstatedir} \
      --sharedstatedir %{_sharedstatedir} \
      --destdir $RPM_BUILD_ROOT
ocaml setup.ml -build

%check
ocaml setup.ml -test

%install
export DESTDIR=$RPM_BUILD_ROOT
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
ocaml setup.ml -install
strip $OCAMLFIND_DESTDIR/stublibs/dll*.so
chrpath --delete $OCAMLFIND_DESTDIR/stublibs/dll*.so

%files
%doc LICENSE.txt
%doc README.md
%{_libdir}/ocaml/inotify
%exclude %{_libdir}/ocaml/inotify/*.a
%exclude %{_libdir}/ocaml/inotify/*.cmxa
%exclude %{_libdir}/ocaml/inotify/*.mli
%exclude %{_libdir}/ocaml/inotify/*.annot
%exclude %{_libdir}/ocaml/inotify/*.cmt
%exclude %{_libdir}/ocaml/inotify/*.cmti
%{_libdir}/ocaml/stublibs/*.so
%{_libdir}/ocaml/stublibs/*.so.owner

%files devel
%doc LICENSE.txt
%doc README.md
%{_libdir}/ocaml/inotify/*.a
%{_libdir}/ocaml/inotify/*.cmxa
%{_libdir}/ocaml/inotify/*.mli

%changelog
* Thu Aug 25 2016 Christian Lindig <christian.lindig@citrix.com> - 2.3-1
- Packaged new upstream release

* Wed Jul 27 2016 Euan Harris <euan.harris@citrix.com> - 2.0-2
- Remove *.cmt, *.cmti and *.annot

* Tue Oct 14 2014 David Scott <dave.scott@citrix.com> - 2.0-1
- Update to 2.0

* Wed Jan 01 2014 Edvard Fagerholm <edvard.fagerholm@gmail.com> - 1.3-1
- Initial package for Fedora 20.
