%define upstream_name    Locale-Maketext
%define upstream_version 1.19

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Framework for software localization
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Locale/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(I18N::LangTags)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
It is a common feature of applications (whether run directly, or via the
Web) for them to be "localized" -- i.e., for them to a present an English
interface to an English-speaker, a German interface to a German-speaker,
and so on for all languages it's programmed with. Locale::Maketext is a
framework for software localization; it provides you with the tools for
organizing and accessing the bits of text and text-processing code that you
need for producing localized applications.

In order to make sense of Maketext and how all its components fit together,
you should probably go read Locale::Maketext::TPJ13, and _then_ read the
following documentation.

You may also want to read over the source for 'File::Findgrep' and its
constituent modules -- they are a complete (if small) example application
that uses Maketext.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc ChangeLog README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Jun 13 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.190.0-1mdv2011.0
+ Revision: 684770
- update to new version 1.19

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 1.170.0-3
+ Revision: 656936
- rebuild for updated spec-helper

* Sat Nov 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.170.0-2mdv2011.0
+ Revision: 597102
- rebuild

* Sat Nov 13 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.170.0-1mdv2011.0
+ Revision: 597084
- new version

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 1.130.0-1mdv2011.0
+ Revision: 401638
- rebuild using %%perl_convert_version
- fixed license field

* Mon May 11 2009 Jérôme Quelin <jquelin@mandriva.org> 1.13-1mdv2010.0
+ Revision: 374537
- import perl-Locale-Maketext


* Mon May 11 2009 cpan2dist 1.13-1mdv
- initial mdv release, generated with cpan2dist

