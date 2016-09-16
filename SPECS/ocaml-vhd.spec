%global debug_package %{nil}

Name:           ocaml-vhd
Version:        0.7.4
Release:        1%{?dist}
Summary:        Pure OCaml library for reading, writing, streaming, converting vhd format files
License:        LGPL2.1 + OCaml linking exception
URL:            https://github.com/djs55/ocaml-vhd
Source0:        https://github.com/djs55/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  ocaml
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-cstruct-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-lwt-devel
BuildRequires:  ocaml-ounit-devel
BuildRequires:  ocaml-uuidm-devel
BuildRequires:  ocaml-io-page-devel
BuildRequires:  ocaml-mirage-types-devel

%description
A pure OCaml parser and printer for vhd format data. The library allows
vhd files to be read, written and streamed with on-the-fly format conversion.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       ocaml-cstruct-devel%{?_isa}
Requires:       ocaml-io-page-devel%{?_isa}
Requires:       ocaml-lwt-devel%{?_isa}
Requires:       ocaml-ounit-devel%{?_isa}
Requires:       ocaml-mirage-types-devel%{?_isa}
Requires:       ocaml-uuidm-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

# The auto-requirements script can't handle packed libraries.
%{?filter_setup:
%filter_from_requires /ocaml(Patterns)/d
%filter_from_requires /ocaml(S)/d
%filter_setup
}


%prep
%setup -q

%build
if [ -x ./configure ]; then
  ./configure
fi
make

%install
mkdir -p %{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
ocaml setup.ml -install


%files
%doc CHANGES
%doc LICENSE
%doc README.md
%{_libdir}/ocaml/vhd-format
%{_libdir}/ocaml/stublibs/dllvhd*
%exclude %{_libdir}/ocaml/vhd-format/*.a
%exclude %{_libdir}/ocaml/vhd-format/*.cmxa
%exclude %{_libdir}/ocaml/vhd-format/*.cmx
%exclude %{_libdir}/ocaml/vhd-format/*.ml
%exclude %{_libdir}/ocaml/vhd-format/*.mli
%exclude %{_libdir}/ocaml/vhd-format/*.annot
%exclude %{_libdir}/ocaml/vhd-format/*.cmt
%exclude %{_libdir}/ocaml/vhd-format/*.cmti


%files devel
%{_libdir}/ocaml/vhd-format/*.a
%{_libdir}/ocaml/vhd-format/*.cmx
%{_libdir}/ocaml/vhd-format/*.cmxa
%{_libdir}/ocaml/vhd-format/*.mli


%changelog

* Tue Sep 13 2016 Zheng Li <zheng.li3@citrix.com> - 0.7.4-1
- Update to 0.7.4 which contains fixes for CA-212154 and CA-218219

* Wed Jul 27 2016 Euan Harris <euan.harris@citrix.com> - 0.7.3-5
- Remove *.cmt, *.cmti and *.annot

* Fri Jun 24 2016 Christian Lindig <christian.lindig@citrix.com> - 0.7.3-4
- drop the previous patch because it contained a bug: when
  lseek(SEEK_HOLE) is retried, the offset must be 0, not c_ofs.
- apply a new, corrected patch

* Thu May 26 2016 Christian Lindig <christian.lindig@citrix.com> - 0.7.3-3
- drop the previous patch because it has two problems: (1) the code doesn't
  compile when the platform doesn't support SEEK_DATA (2) the retry of
  lseek may mask errors.
- apply a new patch that avoids the above problems

* Tue May 24 2016 Christian Lindig <christian.lindig@citrix.com> - 0.7.3-2
- Applied patch https://github.com/djs55/ocaml-vhd/pull/33 for
  runtime support of filesystems without SEEK_DATA support. When lseek
  fails, it is tried again with SEEK_SET.

* Thu Apr 21 2016 Euan Harris <euan.harris@citrix.com> - 0.7.3-1
- Update to 0.7.3

* Thu Oct 2 2014 David Scott <dave.scott@citrix.com> - 0.7.2-1
- Update to 0.7.2

* Tue Apr 1 2014 Euan Harris <euan.harris@citrix.com> - 0.7.0-1
- Update to 0.7.0

* Thu Nov 21 2013 David Scott <dave.scott@eu.citrix.com> - 0.6.4-1
- Update to 0.6.4

* Wed Oct 30 2013 David Scott <dave.scott@eu.citrix.com> - 0.6.1-1
- Update to 0.6.1

* Wed Oct 02 2013 David Scott <dave.scott@eu.citrix.com> - 0.6.0-1
- Initial package

